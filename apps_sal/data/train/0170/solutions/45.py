class Solution:
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
        # equal to max increasing subarray
        seqs = [0]
        last = nums[0]

        for i, num in enumerate(nums[1:]):
            if num < last:
                seqs.append(i + 1)
            last = num
        if len(seqs) == 1:
            return 0

        no_first_size = seqs[-1]
        has_first_size = len(nums) - seqs[1]
        for first_end in range(0, seqs[1]):
            first_size = len(nums)
            for i in range(seqs[-1], len(nums)):
                if nums[i] >= nums[first_end]:
                    first_size = i - first_end - 1
                    break
            has_first_size = min(has_first_size, first_size)
            if first_size == len(nums):
                break
        return min(no_first_size, has_first_size)
