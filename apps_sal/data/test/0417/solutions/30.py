import queue
import math
import copy
'\nN = int(input())\n#S = input()\n# (N,M) = (int(i) for i in input().split(" "))\n# A = [int(i) for i in input().split()]\nA = []\nfor i in range(N):\n\tA.append(int(input()))\n\nprint(A)\n\n'
(N, X, D) = (int(i) for i in input().split(' '))
mp = {}
if D == 0:
    if X == 0:
        ans = 1
    else:
        ans = N + 1
else:
    for i in range(N + 1):
        md = i * X % D
        if not md in mp:
            mp[md] = []
        k = i * (i - 1) // 2
        mp[md].append([k + (i * X - md) // D, 0])
        k = (N * 2 - i - 1) * i // 2
        mp[md].append([k + (i * X - md) // D + 1, 1])
    ans = 0
    for k in mp.keys():
        s = sorted(mp[k])
        md = 0
        bef = 0
        for t in s:
            if md > 0:
                ans += t[0] - bef
            bef = t[0]
            if t[1] == 0:
                md += 1
            else:
                md -= 1
print(ans)
