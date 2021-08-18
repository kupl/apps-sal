class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre = 0
        sums = [0]
        for el in nums:
            pre += el
            sums.append(pre)

        ans = 0
        seen = {}
        for i, v in enumerate(sums):
            if v - target in seen:
                ans += 1
                seen = {}
            seen[v] = i
        return ans
