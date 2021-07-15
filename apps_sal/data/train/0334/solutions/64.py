class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        def find_cost(start, end):
            a = cost[start:end+1]
            a.sort()
            return sum(a[:-1])
        
        res = 0
        if len(s) == 1:
            return res
        
        i = 1
        start = -1
        while i < len(s):
            if s[i-1] == s[i] and start < 0:
                start = i-1
            if s[i] != s[i-1] and start >= 0:
                res += find_cost(start, i-1)
                start = -1
            i += 1
        if start >= 0:
            res += find_cost(start, len(s)-1)       
        
        return res
