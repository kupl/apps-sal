class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stack = []
        ans = 0
        for i, c in enumerate(s):
            if stack and s[stack[-1]] == c:
                if cost[stack[-1]] < cost[i]:
                    ans += cost[stack[-1]]
                    stack.pop()
                    stack.append(i)
                else:
                    ans += cost[i]
            else:
                stack.append(i)
        return ans
