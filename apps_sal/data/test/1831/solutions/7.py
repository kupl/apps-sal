def f(): return map(int, input().split())


n, m = f()
p = list(range(n))


def g(i):
    j = i
    while j != p[j]:
        j = p[j]
    while i != j:
        i, p[i] = p[i], j
    return j


for j in range(m):
    a, b = f()
    p[g(a - 1)] = g(b - 1)

s = g(0)
k = all(g(i) == s for i in p)

print('yes' if m == n - 1 and k else 'no')
