import queue
import math
import copy
"""
N = int(input())
#S = input()
# (N,M) = (int(i) for i in input().split(" "))
# A = [int(i) for i in input().split()]
A = []
for i in range(N):
	A.append(int(input()))

print(A)

"""

(N, X, D) = (int(i) for i in input().split(" "))
mp = {}
if D == 0:
    if X == 0:
        ans = 1
    else:
        ans = N + 1
else:
    for i in range(N + 1):
        md = (i * X) % D
        if not md in mp:
            mp[md] = []
        k = i * (i - 1) // 2
        mp[md].append([k + (((i * X) - md) // D), 0])
        k = (N * 2 - i - 1) * i // 2
        mp[md].append([k + (((i * X) - md) // D) + 1, 1])
    # print(mp)
    ans = 0
    for k in mp.keys():
        s = sorted(mp[k])
        # print(s)
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
