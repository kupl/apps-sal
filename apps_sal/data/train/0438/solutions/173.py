class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        da = {}
        db = {}
        n = len(arr)
        s = [0 for i in range(len(arr))]
        cnts = 0
        step = 0
        for e in arr:
            step += 1
            x = e-1
            s[x] = 1
            st = x
            ed = x
            da[x] = (x, x)
            db[x] = (x, x)
            if x > 0 and s[x-1] == 1:
                p = db[x-1]
                if (p[1]+1-p[0] == m):
                    cnts -= 1
                st = p[0]
                da[st] = (st, ed)
                del db[p[1]]
                db[ed] = (st, ed)
                del da[x]
            if x < n-1 and s[x+1] == 1:
                q = da[x+1]
                if (q[1]+1-q[0] == m):
                    cnts -= 1
                ed = q[1]
                da[st] = (st, ed)
                del da[q[0]]
                db[ed] = (st, ed)
                del db[x]

            if (ed+1-st) == m:
                cnts += 1
            if cnts > 0:
                ans = step

        return ans
