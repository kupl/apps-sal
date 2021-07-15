class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        ta = [-1] * n
        sg = [-1] * n
        eg = [-1] * n
        g = {}
        ans = -1
        gc = {}
        for step, v in enumerate(arr):
            idx = v - 1
            wl = False
            wr = False
            if idx > 0 and eg[idx-1] > -1:
                sgi = eg[idx-1]
                ngl = g[sgi]
                sg[sgi] = idx
                eg[idx] = sgi
                g[sgi] += 1
                gc[ngl] -= 1
                if ngl+1 not in gc:
                    gc[ngl+1] = 0
                gc[ngl+1] += 1
                wl = True
            if idx < n-1 and sg[idx+1] > -1:
                sgi = idx+1
                egi = sg[sgi]
                ngl = g[sgi]
                eg[egi] = idx
                sg[idx] = egi
                g[idx] = g[sgi]+1
                l = g.pop(sgi)
                gc[ngl] -= 1
                if ngl+1 not in gc:
                    gc[ngl+1] = 0
                gc[ngl+1] += 1
                wr = True
            if not wl and not wr:
                sg[idx] = idx
                eg[idx] = idx
                g[idx] = 1
                if 1 not in gc:
                    gc[1] = 0
                gc[1] += 1
            elif wl and wr:
                sgi = eg[idx]
                ngl = g[sgi]
                ngr = g[idx]
                l = g.pop(idx)
                gc[ngl] -= 1
                gc[ngr] -= 1
                if ngl+ngr-1 not in gc:
                    gc[ngl+ngr-1] = 0
                gc[ngl+ngr-1] += 1
                g[sgi] = g[sgi] + l - 1
                egi = sg[idx]
                eg[egi] = sgi
                sg[sgi] = egi
            ta[idx] = v

            if m in gc and gc[m] > 0:
                ans = step+1

            step += 1
        return ans
