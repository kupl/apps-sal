class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [-1]
        for i in range(len(nums)):
            if nums[i] & 1:
                odds.append(i)  # &1 should be faster than %2
        odds.append(len(nums))
        i, count = 1, 0
        while i + k - 1 < len(odds) - 1:
            count += (odds[i] - odds[i - 1]) * (odds[i + k] - odds[i + k - 1])
            i += 1
        return count
