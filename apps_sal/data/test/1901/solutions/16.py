def R(): return list(map(int, input().split()))


n, m = R()
p = [i for i in range(n + 1)]


def find(i):
    while p[i] != i:
        p[i] = p[p[i]]
        i = p[i]
    return i


c = [0] + list(R())
for _ in range(m):
    x, y = list(map(find, R()))
    if c[x] < c[y]:
        x, y = y, x
    p[x] = y
print(sum(c[i] for i in range(n + 1) if p[i] == i))
