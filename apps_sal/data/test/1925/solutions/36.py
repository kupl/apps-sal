import math

a, b, n = map(int, input().split())

ans = math.floor(a * min(b - 1, n) / b)

print(ans)
