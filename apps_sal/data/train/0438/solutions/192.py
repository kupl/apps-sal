class Solution:
    def findLatestStep(self, arr: List[int], target: int) -> int:
        b = [0] * len(arr)
        m = {}
        c = {}
        res = -1
        step = 1
        for i in arr:
            i -= 1
            newl = i
            newr = i
            if i >= 1 and b[i - 1] == 1:
                l = i - m[i - 1]
                newl = m[i - 1]
                del m[m[i - 1]]
                if i - 1 in m:
                    del m[i - 1]
                c[l] -= 1
            if i < len(arr) - 1 and b[i + 1] == 1:
                l = m[i + 1] - i
                newr = m[i + 1]
                del m[m[i + 1]]
                if i + 1 in m:
                    del m[i + 1]
                c[l] -= 1
            m[newl] = newr
            m[newr] = newl
            l = newr - newl + 1
            c[l] = c.get(l, 0) + 1
            b[i] = 1
            if c.get(target, 0):
                res = step
            step += 1
        return res
