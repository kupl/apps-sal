import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))


n, m, l = rint()
a = list(rint())

seg_cnt = 0
for i in range(1, n):
    if a[i - 1] > l and a[i] <= l:
        seg_cnt += 1
if a[n - 1] > l:
    seg_cnt += 1


for i in range(m):
    t = list(rint())
    if t[0] == 0:
        print(seg_cnt)
    else:
        p = t[1] - 1
        d = t[2]
        if a[p] + d > l and a[p] <= l:
            if p == 0:
                if a[(p + 1) % n] <= l:
                    seg_cnt += 1
            elif p == n - 1:
                if a[p - 1] <= l:
                    seg_cnt += 1
            else:
                if a[p - 1] > l and a[(p + 1) % n] > l:
                    seg_cnt -= 1
                elif a[p - 1] <= l and a[(p + 1) % n] <= l:
                    seg_cnt += 1
        a[p] += d
