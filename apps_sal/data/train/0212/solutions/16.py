class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        d = {}
        MOD = 1000000007
        for a in A:
            d[a] = 1 + sum(d[a//b] * d[b] for b in d if not a%b and a//b in d)
        #print(d)
        return sum(d.values()) % MOD
