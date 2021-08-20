(n, m) = list(map(int, input().split()))
ok = m == n - 1
dsu = list(range(n))


def get(x):
    y = x
    while y != dsu[y]:
        y = dsu[y]
    while x != y:
        z = dsu[x]
        dsu[x] = y
        x = z
    return y


for i in range(m):
    (a, b) = [int(x) - 1 for x in input().split()]
    dsu[get(a)] = get(b)
for i in range(n):
    get(i)
ok &= max(dsu) == min(dsu)
print('yes' if ok else 'no')
