from math import *
n, k = list(map(int, input().split()))
val = int(sqrt(9 + (8 * (n + k))))
ans = (-3 + val) // 2
print(n - ans)
