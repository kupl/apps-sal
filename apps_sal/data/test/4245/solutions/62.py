import math

A, B = list(map(int, input().split()))

ans = math.ceil((B - 1) / (A - 1))

if B <= 1:
    print((0))
else:
    print(ans)
