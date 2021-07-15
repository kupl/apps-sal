import math
N,T=map(int, input().split())
ans = math.inf
for i in range(N):
    c,t=map(int,input().split())
    if t <= T:
        ans = min(ans, c)
print(ans if ans != math.inf else "TLE")
