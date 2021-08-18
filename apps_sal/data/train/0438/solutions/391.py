class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        sele = [0] * n
        repe = [i for i in range(n)]
        sis = [1] * n

        def getRepe(a):
            if repe[a] == a:
                return a
            repe[a] = getRepe(repe[a])
            return repe[a]

        def join(a, b):
            ra, rb = getRepe(a), getRepe(b)
            repe[b] = ra
            sis[ra] += sis[rb]

        def sete(x):
            if x > 0 and sele[x - 1]:
                join(x - 1, x)
            if x < n - 1 and sele[x + 1]:
                join(x, x + 1)
            sele[x] = 1
        res = -1
        for i, v in enumerate(arr, 1):
            if v > 1 and sele[v - 2] and sis[getRepe(v - 2)] == m:
                res = i - 1
            if v < n and sele[v] and sis[getRepe(v)] == m:
                res = i - 1
            sete(v - 1)
            if sis[getRepe(v - 1)] == m:
                res = i
        return res
