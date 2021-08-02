N, T = map(int, input().split())
mi = 1001
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if c <= mi: mi = c
if mi == 1001: print("TLE")
else: print(mi)
