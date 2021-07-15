class Solution:
    def clumsy(self, N: int) -> int:
        res = None
        while N > 0:
            val = N
            N -= 1
            print(N, val, res)
            if N > 0:
                val = val * N
                N -= 1
            print(N, val, res)
            if N > 0:
                val = val // N
                N -= 1
            print(N, val, res)
            if res is None:
                if N > 0:
                    val = val + N
                    N -= 1
                print(N, val, res)
                res = val
            else:
                if N > 0:
                    val = val - N
                    N -= 1
                print(N, val, res)
                res -= val
            print(N, val, res)
        return res
