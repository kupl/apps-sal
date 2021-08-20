def find(w, m, d, l):
    s = 0
    c = 1
    for i in range(l):
        s += w[i]
        if s > m:
            s = w[i]
            c += 1
        if c > d:
            return False
    return True


class Solution:

    def shipWithinDays(self, w: List[int], D: int) -> int:
        l = len(w)
        s = max(w)
        e = sum(w)
        m = s + (e - s) // 2
        p = 0
        while s <= e:
            a = find(w, m, D, l)
            if a == True:
                p = m
                e = m - 1
                m = s + (e - s) // 2
            else:
                s = m + 1
                m = s + (e - s) // 2
        return p
