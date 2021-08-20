class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        A.sort()
        parents = dict()
        seen = set()
        for a in A:
            tot = 1
            for s in seen:
                if a % s == 0:
                    b = a // s
                    if b in seen:
                        tot += parents[s] * parents[b]
            parents[a] = tot
            seen.add(a)
        return sum(parents.values()) % mod
