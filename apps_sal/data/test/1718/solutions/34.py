import math
n, k = map(int, input().split())
a = list(map(int, input().split()))

start = a.index(1)

left = start

x = math.ceil(left / (k - 1))
excess = x * (k - 1) - left

right = max((n - start - 1 - excess), 0)

y = math.ceil(right / (k - 1))

print(x + y)
