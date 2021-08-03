class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        n = len(A)
        A.sort()
        s = {a: i for i, a in enumerate(A)}
        d = collections.defaultdict(set)
        for i in range(n):
            for j in range(i):
                if A[i] % A[j] == 0:
                    res = A[i] // A[j]
                    if res in s:
                        d[i].add((j, s[res]))

        @lru_cache(maxsize=None)
        def dfs(i):
            nonlocal ans
            cur = 1
            for l, r in d[i]:
                cur += dfs(l) * dfs(r)
            return cur
        ans = 0
        for i in range(n):
            val = dfs(i)
            ans += val
        return ans % 1000000007
