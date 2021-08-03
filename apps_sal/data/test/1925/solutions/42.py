import math
A, B, N = map(int, input().split())

if B > N:
    ans = math.floor(A * N / B)
else:
    ans = math.floor(A * (B - 1) / B)

print(ans)
