class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        i = 0
        mod = (int)(1e9+7)
        while i < len(s):
            if s[i]!='1':
                i+=1
                continue
            start = i
            while i<len(s) and s[i] == '1':
                i+=1
            count = i-start
            res += count*(count+1)/2
            res %= mod
        
        return int(res)

