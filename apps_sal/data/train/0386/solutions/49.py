class Solution:
    
    
    def countVowelPermutation(self, n: int) -> int:
        
        d = {}
        d['a'] = 1
        d['e'] = 1
        d['i'] = 1
        d['o'] = 1
        d['u'] = 1
        
        for i in range(1,n):
            dx = {}
            dx['a'] = (d['e'] + d['i'] + d['u']) % (10**9+7)
            dx['e'] = (d['a'] + d['i']) % (10**9+7)
            dx['i'] = (d['e'] + d['o']) % (10**9+7)
            dx['o'] = (d['i']) % (10**9+7)
            dx['u'] = (d['i'] + d['o']) % (10**9+7)
            d = dx
        
        r = 0
        for c in d.keys():
            r += (d[c] % (10**9+7))
            
        return r % (10**9+7)
