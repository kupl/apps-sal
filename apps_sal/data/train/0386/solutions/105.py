class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prevfreq = {'a':1, 'e':1, 'o':1, 'i':1, 'u':1}
        vmap = {'a':['e'], 'e':['a','i'], 'i':['a','e','o','u'], 'o':['i','u'], 'u':['a']}
        for i in range(1, n):
            # print(i)
            curfreq = defaultdict(int)
            for v, freq in prevfreq.items():
                # print(v,freq)
                for nextv in vmap[v]:
                    curfreq[nextv] += freq
                    # print(curfreq)
            prevfreq = curfreq
        return sum(prevfreq.values()) % (10**9+7)
