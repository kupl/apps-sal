class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def AtMostK(k):
            left = 0
            count = 0
            currK = 0
            for index in range(len(nums)):
                if nums[index] % 2 == 1:
                    currK += 1
                while currK > k:
                    if nums[left] % 2 == 1:
                        currK -= 1
                    left += 1
                count += index - left + 1
            return count
        return AtMostK(k) - AtMostK(k - 1)
