# author:  Taichicchi
# created: 11.10.2020 10:52:46

import sys

N, T = list(map(int, input().split()))

ans = 100000
for i in range(N):
    c, t = list(map(int, input().split()))
    if t <= T:
        ans = min(ans, c)

if ans == 100000:
    print("TLE")
else:
    print(ans)
