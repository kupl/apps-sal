class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        d = {'a':1,'e':2,'i':3,'o':4,'u':5}
        
        @lru_cache(maxsize=None)
        def f(n, i):
            if n == 0:
                return 1
            if i == d['a']:
                return f(n-1, d['e'])
            if i == d['e']:
                return f(n-1, d['a']) + f(n-1, d['i'])
            if i == d['i']:
                return f(n-1, d['a']) + f(n-1, d['e']) + f(n-1, d['o']) + f(n-1, d['u'])
            if i == d['o']:
                return f(n-1, d['i']) + f(n-1, d['u'])
            if i == d['u']:
                return f(n-1, d['a'])
            
        if n == 0: return 0
        ans = 0
        for k, v in d.items():
            ans += f(n-1, v)
        return ans % (10**9 + 7)
