class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        idx = 0
        left = 0
        while idx < len(s):
            while idx + 1 < len(s) and s[idx] == s[idx + 1]:
                idx += 1
            if left < idx:
                ans += sum(cost[left:idx + 1]) - max(cost[left:idx + 1])
            idx += 1
            left = idx

        return ans
