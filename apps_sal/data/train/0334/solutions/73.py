class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0

        n = len(s)
        stack = []
        i = 0
        while i < n:
            c = s[i]
            if stack and s[stack[-1]] == c:
                j = stack.pop()
                prev_cost = cost[j]
                if prev_cost < cost[i]:
                    stack.append(i)
                else:
                    stack.append(j)
                res += min(prev_cost, cost[i])
                i += 1
            else:
                stack.append(i)
                i += 1
        return res
