__author__ = 'Utena'
n, a = map(int, input().split())
cities = [0] + list(map(int, input().split()))
p = [0] * n
c = [0] * n
for i in range(n):
    if i == 0: p[i] = 1
    elif i <= min(n - a, a - 1): p[i] = 2
    elif min(n - a, a - 1) < i <= max(n - a, a - 1): p[i] = 1
    else: p[i] = 0
for i in range(1, n + 1):
    c[abs(a - i)] += cities[i]
t = 0
for i in range(n):
    if c[i] == p[i]:
        t += c[i]
print(t)
