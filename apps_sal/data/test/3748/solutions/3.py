import sys
import copy
sys.setrecursionlimit(10 ** 6)


def main():

    def per(s, a=[]):
        if not s:
            return [a]
        if len(s) % 2:
            cs = copy.deepcopy(s)
            res = []
            for u in cs:
                s.remove(u)
                res += per(s, [u] + a)
                s.add(u)
            return res
        u = min(s)
        s.remove(u)
        cs = copy.deepcopy(s)
        res = []
        for uu in cs:
            if uu < u:
                continue
            s.remove(uu)
            res += per(s, a + [u, uu])
            s.add(uu)
        s.add(u)
        return res
    ord_a = ord('a')
    (h, w) = list(map(int, input().split()))
    t0 = [[ord(c) - ord_a for c in input()] for _ in range(h)]
    h_set = set(range(h))
    pattern = per(h_set)
    b = h % 2
    for p in pattern:
        t1 = [[] for _ in range(h)]
        if b:
            t1[h // 2] = t0[p[0]]
        i = 0
        for ii in range(b, h, 2):
            t1[i] = t0[p[ii]]
            t1[h - 1 - i] = t0[p[ii + 1]]
            i += 1
        fin = [False] * w
        mid = w % 2 == 1
        br = False
        for (j, c0) in enumerate(zip(*t1)):
            if fin[j]:
                continue
            fin[j] = True
            c0 = c0[::-1]
            for (jj, c1) in enumerate(zip(*t1)):
                if jj <= j:
                    continue
                if fin[jj]:
                    continue
                if c0 == c1:
                    fin[jj] = True
                    break
            else:
                if mid and c0 == c0[::-1]:
                    mid = False
                else:
                    br = True
                    break
        if br:
            continue
        print('YES')
        return
    print('NO')


main()
