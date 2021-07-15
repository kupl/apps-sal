import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    n, I = list(map(int, input().split()))
    a = list(map(int, input().split()))
    K = 2**min(20, 8*I//n)

    a.sort()
    c = []
    pos = 0
    while pos < n:
        r = pos
        while r+1 < n and a[pos] == a[r+1]:
            r += 1
        c.append(r-pos+1)
        pos = r + 1

    if K > len(c):
        print(0)
    else:
        pref = c.copy()
        suff = c.copy()
        for i in range(1, len(c)):
            pref[i] += pref[i-1]
        for i in range(len(c)-2, -1, -1):
            suff[i] += suff[i+1]

        res = sum(c)
        l = 0
        r = K-1
        while r < len(c):
            s1 = 0 if l == 0 else pref[l-1]
            s2 = 0 if r == len(c)-1 else suff[r+1]
            res = min(res, s1+s2)
            l += 1
            r += 1

        print(res)

def __starting_point():
    main()

__starting_point()
