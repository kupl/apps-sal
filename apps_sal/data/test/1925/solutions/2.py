import math

A, B, N = list(map(int, input().split()))

if N >= B:
    x = B-1
else:
    x = N

ans = math.floor(A*x/B) - A*math.floor(x/B)

print(ans)

