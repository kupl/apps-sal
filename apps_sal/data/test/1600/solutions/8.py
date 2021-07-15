__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/C.in', 'r')
T = 1

def process():
    N = int(input())
    h = list(map(int, input().split()))

    hpx = []
    last = {}
    for i, v in enumerate(h): hpx.append([v, i])
    hpx = sorted(hpx, key=lambda x:x[0])
    maxp = -1
    i = 0
    while i < N:
        item = hpx[i]
        v = item[0]
        j = i
        while j < N and hpx[j][0] == v:
            p = hpx[j][1]
            last[p] = max(maxp, p)
            j = j + 1

        j = i
        while j < N and hpx[j][0] == v:
            p = hpx[j][1]
            maxp = max(maxp, p)
            j = j + 1
        i = j

    ans = 0
    p = 0
    while p < N:
        ans = ans + 1
        nextp = p + 1

        while p < N and p < nextp:
            nextp = max(nextp, last[p] + 1)
            p = p + 1

    print(ans)




for _ in range(T):
    process()

