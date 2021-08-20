class Solution:

    def clumsy(self, N: int) -> int:
        self.N = N
        k = N // 4
        r = N % 4

        def result(n):
            if r == 1:
                return 1
            elif r == 2:
                return 2
            elif r == 3:
                return 6
            elif r == 0:
                return 5
        cFac = 2 * (N - 1)
        if N < 4:
            return result(r)
        elif N == 4:
            cFac += 1
        else:
            if r == 0:
                cFac += -4 * (k - 2)
            else:
                cFac += -4 * (k - 1)
            cFac -= result(r)
        return cFac
