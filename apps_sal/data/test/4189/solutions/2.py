from math import sqrt
n = int(input())

s, h = 0, 0
for i in range(n):
    a, b = input().split()
    if b == 'soft':
        s += 1
    else:
        h += 1

k = 2 * max(s, h) - 1
if s + h > k:
    k += 1

t = int(sqrt(k))
if t * t < k:
    t += 1
print(t)
