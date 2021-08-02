import math

k, n, w = map(int, input().split(' '))
total = 0
for i in range(w):
    total += (i + 1) * k

if total <= n:
    print(0)
else:
    print(total - n)
