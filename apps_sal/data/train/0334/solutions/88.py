class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        stack = []
        idx = 0
        while idx < len(s):
            while idx < len(s) - 1 and s[idx] == s[idx+1]:
                stack.append(cost[idx])
                idx += 1
            if idx > 0 and s[idx] == s[idx-1]:
                stack.append(cost[idx])
            if stack:
                res += (sum(stack) - max(stack))
                stack = []
            idx += 1
        return res
