class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        hd, td = {}, {}
        ld = {}
        n = -1
        for k, i in enumerate(arr):
            if i-1 in td and i+1 in hd:
                h = td[i-1]
                t = hd[i+1]
                hd[h] = t
                td[t] = h
                del hd[i+1]
                del td[i-1]
                ld[t-i] = ld[t-i]-1
                ld[i-h] = ld[i-h]-1
                if t-h+1 not in ld:
                    ld[t-h+1] = 0
                ld[t-h+1] = ld[t-h+1] + 1
            elif i-1 in td:
                h = td[i-1]
                hd[h] = i
                td[i] = h
                del td[i-1]
                ld[i-h] = ld[i-h] - 1
                if i-h+1 not in ld:
                    ld[i-h+1] = 0
                ld[i-h+1] = ld[i-h+1] + 1
            elif i+1 in hd:
                t = hd[i+1]
                hd[i] = t
                td[t] = i
                del hd[i+1]
                ld[t-i] = ld[t-i] - 1
                if t-i+1 not in ld:
                    ld[t-i+1] = 0
                ld[t-i+1] = ld[t-i+1] + 1
            else:
                hd[i] = i
                td[i] = i
                if 1 not in ld:
                    ld[1] = 0
                ld[1] = ld[1] + 1
            if m in ld and ld[m] > 0:
                n = k+1
        return n

