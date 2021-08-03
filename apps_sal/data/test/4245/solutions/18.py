import math

A, B = list(map(int, input().split()))

ans = math.ceil((B - 1) / (A - 1))
print(ans)
