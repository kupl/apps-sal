class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stack = []
        
        res = 0
        for i in range(len(cost)):
            if not stack or s[stack[-1]] != s[i]:
                stack.append(i)
            else:
                if stack and s[stack[-1]] == s[i]:
                    idx = stack.pop()
                    if cost[idx] >= cost[i]:
                        res += cost[i]
                        stack.append(idx)
                    else:
                        res += cost[idx]
                        stack.append(i)
        return res
                
                

