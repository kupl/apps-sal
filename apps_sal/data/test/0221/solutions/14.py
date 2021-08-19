import math
(n, k) = map(int, input().split())
a = math.ceil(n / (2 * k + 1))
print(a)
x = a * (2 * k + 1) - n
if x >= k:
    start = 1
else:
    start = 1 + (k - x)
for i in range(start, n + 1, 2 * k + 1):
    print(i, end=' ')
