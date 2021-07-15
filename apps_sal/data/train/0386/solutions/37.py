class Solution:
    def countVowelPermutation(self, n: int) -> int:
        graph = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o':['i', 'u'], 'u':['a']}
        d1={'a':1, 'e':1, 'i':1,'o':1,'u':1}
        
        for i in range(1,n):
            d2={}
            for v, f in d1.items():
                for nxt in graph[v]: 
                    d2[nxt] = d2.get(nxt, 0) + f
            d1 = d2
        return sum(d1.values()) % (10**9+7)
