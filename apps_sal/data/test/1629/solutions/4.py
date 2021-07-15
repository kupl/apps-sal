from math import inf

n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
x -= 1

mx = inf
mi = None
for i in range(x, x - n, -1):
    if a[i] < mx:
        mx = a[i]
        mi = i

mi %= n

for i in range(n):
    a[i] -= mx

a[mi] = mx * n + (x - mi) % n

for i in range(mi + 1 - (n if x < mi else 0), x + 1):
    a[i] -= 1

print(' '.join(map(str, a)))


