from collections import Counter


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCounts = []
        oddCount = 0
        for num in nums:
            if num % 2 == 1:
                oddCount += 1
            oddCounts.append(oddCount)
        oddCountsIdxs = Counter(oddCounts)
        nice = 0
        for num in oddCounts:
            nice += oddCountsIdxs[num - k]
        nice += oddCountsIdxs[k]
        return nice
