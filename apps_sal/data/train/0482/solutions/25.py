class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        self.cache = {}

        def dp(i, j):
            if (i, j) not in self.cache:
                if i == j:
                    ret = arr[i], 0
                else:
                    best_p, best_s = 2**32, 2**32
                    for k in range(i, j):

                        l1, s1 = dp(i, k)
                        l2, s2 = dp(k + 1, j)

                        if s1 + s2 + l1 * l2 < best_s:
                            best_p = max(l1, l2)
                            best_s = s1 + s2 + l1 * l2

                    ret = best_p, best_s

                self.cache[(i, j)] = ret
            return self.cache[(i, j)]

        return dp(0, len(arr) - 1)[-1]
