class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        (res, n, cache, sv) = (0, len(A), collections.defaultdict(int), 0)
        cache[0] = 1
        for (i, v) in enumerate(A):
            sv += v
            if cache[sv % K] > 0:
                res += cache[sv % K]
            cache[sv % K] += 1
        return res
