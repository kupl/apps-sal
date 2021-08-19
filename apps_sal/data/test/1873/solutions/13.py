__author__ = 'Utena'
(n, m) = map(int, input().split())
s = list(map(int, input().split()))
v = [0] * m
for i in s:
    v[i - 1] += 1
t = 0
for j in range(m):
    t1 = v[j]
    t2 = 0
    for r in range(j + 1, m):
        t2 += t1 * v[r]
    t += t2
print(t)
