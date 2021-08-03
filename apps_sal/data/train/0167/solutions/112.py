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
            if st > N:
                v_st = math.inf
                v_end = 1 + max(find(k - 1, end - 1), find(k, n - end))
            elif end < 1:
                v_end = math.inf
                v_st = 1 + max(find(k - 1, st - 1), find(k, n - st))
            else:
                v_st = 1 + max(find(k - 1, st - 1), find(k, n - st))
                v_end = 1 + max(find(k - 1, end - 1), find(k, n - end))

            m[k][n] = min(v_st, v_end)
            return m[k][n]

        return find(K, N)
