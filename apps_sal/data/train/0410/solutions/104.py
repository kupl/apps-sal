class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def process(x, nsteps):
            if x == 2:
                return nsteps
            elif x % 2 == 0:
                return process(x // 2, nsteps + 1)
            else:
                return process(x * 3 + 1, nsteps + 1)

        sol = []
        for i in range(lo, hi + 1):
            sol.append((process(i, 0), i))
        sol.sort()
        return sol[k - 1][1]
