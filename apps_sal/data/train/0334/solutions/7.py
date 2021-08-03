class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        _min = 0
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append((s[i], i))
            else:
                t = stack[-1]
                if t[0] == s[i]:
                    if cost[i] > cost[t[1]]:
                        stack.pop()
                        _min += cost[t[1]]
                        stack.append((s[i], i))
                    else:
                        stack.pop()
                        _min += cost[i]
                        stack.append((s[i], t[1]))
                else:
                    stack.append((s[i], i))

        return _min
