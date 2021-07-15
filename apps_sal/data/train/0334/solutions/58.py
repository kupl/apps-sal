class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s:
            return 0
        
        res = 0
        max_idx = 0 # the idx of the max cost value in the consecutive subsequence
        for i in range(1, len(s)):
            if s[i] == s[max_idx]:
                if cost[max_idx] < cost[i]:
                    res += cost[max_idx]
                    max_idx = i
                else:
                    res += cost[i]
            else:
                max_idx = i
        return res
