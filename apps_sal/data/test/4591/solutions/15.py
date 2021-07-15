import math

A, B, C, X, Y = map(int, input().split())

ans = A * X + B * Y

if (A + B) / 2 < C:
    pass
else:
    for i in range(max(X * 2, Y * 2)+1):
        j = max(0, X - int(i / 2))
        k = max(0, Y - int(i / 2))

        ans = min(ans, i * C + j * A + k * B)

print(ans)
