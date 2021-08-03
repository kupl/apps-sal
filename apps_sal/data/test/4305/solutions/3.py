import math
H, A = map(int, input().split())

# H/A の切り上げ
# ceil or (H+A−1)/A の切り捨て
print((H + A - 1) // A)
