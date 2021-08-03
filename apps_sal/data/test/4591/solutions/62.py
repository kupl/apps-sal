import math

A, B, C, X, Y = list(map(int, input().split()))

min_sum = A * X + B * Y
for c in range(0, (max(X, Y) * 2) + 1, 2):
    s = (max(X - math.floor(c / 2), 0)) * A + (max(Y - math.floor(c / 2), 0)) * B + c * C
    if s < min_sum:
        min_sum = s
print(min_sum)
