class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) <= 1:
            return 0
        res = 0
        start = 0
        while True:
            if start >= len(s):
                break
            temp = start + 1
            for i in range(temp, len(s)):
                if s[i] != s[start]:
                    start += 1
                else:
                    break
            if start == len(s) - 1:
                break
            end = start + 2
            while end < len(s):
                if s[end] == s[start]:
                    end += 1
                else:
                    break
            res += (sum(cost[start:end]) - max(cost[start:end]))
            start = end
        return res
        '''
        start = -1
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                start = i-1
                break
        if start==-1: return 0
        end = start+2
        SUM = cost[start]+cost[start+1]
        MAX = max(cost[start], cost[start+1])
        while end<len(s):
            if s[end]==s[start]:
                SUM += cost[end]
                MAX = max(cost[end], MAX)
                end += 1
            else:
                break
        res += (SUM-MAX)
        return res+self.minCost(s[end:], cost[end:])
        '''
