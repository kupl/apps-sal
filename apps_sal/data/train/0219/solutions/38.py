class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        s = 0
        maxLen = 0
        seen = {}
        for idx, hour in enumerate(hours):
            if hour > 8:
                s += 1
            else:
                s -=1
            if s > 0:
                res = idx + 1
                maxLen = max(maxLen, res)
            else:
                if (s-1) in seen:
                    res = (idx - seen[s-1])
                    maxLen = max(maxLen, res)
            
            if s not in seen:
                seen[s] = idx
        return maxLen         
                
            

