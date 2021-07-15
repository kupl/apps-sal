class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0

        n = len(s)
        # while i < n:
        # if i  + 1 < n and s[i] == s[i + 1]:
        stack = []
        # for i, c in enumerate(s):
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
            # print(stack, i, c, res)
            # if not stack:
            #     stack.append(i)
            #     i += 1
            # else:
            #     i += 1
        # print(res)
        return res
