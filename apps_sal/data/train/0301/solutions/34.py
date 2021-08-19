class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        ga = collections.defaultdict(list)
        for (i, v) in enumerate(A):
            ga[v].append(i)

        def pd(i, start_a):
            if i >= len(B) or start_a >= len(A):
                return 0
            if (i, start_a) in memo:
                return memo[i, start_a]
            res = pd(i + 1, start_a)
            if B[i] in ga:
                new_start_a = -1
                for cand in ga[B[i]]:
                    if cand > start_a:
                        new_start_a = cand
                        break
                if new_start_a >= start_a:
                    res = max(res, 1 + pd(i + 1, new_start_a))
            memo[i, start_a] = res
            return res
        memo = dict()
        return pd(0, -1)
