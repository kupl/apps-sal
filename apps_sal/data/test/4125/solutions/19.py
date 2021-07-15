import math, sys
N, X = map(int,input().split())
x = list(map(int, input().split()))
Distance = [abs(X-x[i]) for i in range(N)]

if N ==1:
    print(abs(X-x[0]))
    return

ans = 0
for i in range(N):
    ans = math.gcd(ans, Distance[i])

print(ans)
