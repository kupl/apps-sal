class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        mp = defaultdict(list)
        for i, a in enumerate(A):
            mp[a].append(i)

        @lru_cache(None)
        def dp(i, diff=None):
            res = 1
            if diff is None:
                for j in range(i):
                    res = max(res, 1 + dp(j, A[i] - A[j]))
            else:
                for j in mp[A[i] - diff]:
                    if j < i:
                        res = max(res, 1 + dp(j, diff))
            return res

        return max([dp(i) for i in range(len(A))])
