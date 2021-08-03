class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        res = -1
        x = 0
        n = len(A)
        l2c = {i: 0 for i in range(1, n + 1)}
        d = {}
        for i in range(1, n + 1):
            j = A[i - 1]
            start = end = j
            if j - 1 in d:
                start = d[j - 1][0]
                l = d[j - 1][-1] - d[j - 1][0] + 1
                l2c[l] -= 1
            if j + 1 in d:
                end = d[j + 1][1]
                l = d[j + 1][-1] - d[j + 1][0] + 1
                l2c[l] -= 1
            d[start] = [start, end]
            d[end] = [start, end]
            l2c[end - start + 1] += 1
            if l2c[m] > 0:
                res = i
        return res

    def findLatestStep1(self, A: List[int], m: int) -> int:
        res = -1
        x = 0
        n = len(A)
        for i in range(1, n + 1):
            j = A[i - 1]
            k = 1 << (n - j)
            x += k
            s = bin(x)[2:]
            ss = s.split('0')
            if any(len(s2) == m for s2 in ss):
                res = i
        return res
