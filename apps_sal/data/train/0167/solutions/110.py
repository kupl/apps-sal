class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        m = [[0 for i in range(N + 1)] for j in range(K + 1)]

        def find(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if m[k][n] > 0:
                return m[k][n]

            def bsearch():
                st, end = 1, n
                while st <= end:
                    m = (st + end) // 2
                    if predicate(m):
                        end = m - 1
                    else:
                        st = m + 1
                return st, end

            def predicate(x):
                return True if find(k - 1, x - 1) >= find(k, n - x) else False

            st, end = bsearch()
            v_st = max(find(k - 1, st - 1), find(k, n - st)) if st <= N else math.inf
            v_end = max(find(k - 1, end - 1), find(k, n - end)) if end >= 1 else math.inf

            m[k][n] = min(v_st, v_end) + 1
            return m[k][n]

        return find(K, N)
