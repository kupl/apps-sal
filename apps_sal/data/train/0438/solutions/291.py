class Solution:
    def findLatestStep(self, arr, m):
        D = dict()

        c, ret = 0, -1
        for k, x in enumerate(arr, 1):
            D[x], S = 0, 0

            if x - 1 in D and x + 1 in D:
                i, j = D[x - 1], -D[x + 1]
                if i + 1 == m:
                    c -= 1
                if j + 1 == m:
                    c -= 1
                S = i + j + 2
                D[x - i - 1], D[x + j + 1] = -S, S
            elif x - 1 in D:
                i = D[x - 1]
                if i + 1 == m:
                    c -= 1
                S = i + 1
                D[x - i - 1], D[x] = -S, S
            elif x + 1 in D:
                j = -D[x + 1]
                if j + 1 == m:
                    c -= 1
                S = j + 1
                D[x + j + 1], D[x] = S, -S

            if S + 1 == m:
                c += 1
            if c > 0:
                ret = k

        return ret
