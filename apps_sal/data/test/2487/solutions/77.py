n = int(input())
es = [[0, 0]] * (n - 1)
for i in range(n - 1):
    (u, v) = [int(x) - 1 for x in input().split()]
    (u, v) = (min(u, v), max(u, v))
    es[i] = [u, v]
sv = 0
for i in range(n):
    sv += (i + 1) * (n - i)
se = 0
for (u, v) in es:
    se += (u + 1) * (n - v)
print(sv - se)
