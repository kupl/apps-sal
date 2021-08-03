class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        occur = collections.defaultdict(int)

        occur[0] = 1
        runsum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
            runsum += nums[i]
            if (runsum - k) in occur:
                count += occur[runsum - k]

            occur[runsum] += 1

        return count
