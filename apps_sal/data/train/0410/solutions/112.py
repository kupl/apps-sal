class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def key_func(val):

            def recur(val):
                if val <= 1:
                    return 0
                if val % 2 == 0:
                    return recur(val / 2) + 1
                return recur(val * 3 + 1) + 1
            return recur(val)
        out = [i for i in range(lo, hi + 1)]
        out.sort(key=key_func)
        return out[k - 1]
