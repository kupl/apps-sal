f = []


def mdy(l, r, x):
    f[l] += x
    f[r + 1] -= x


n, m = map(int, input().split())

P = list(range(n + 2))

for i in range(n + 5):
    f.append(0)

a = list(map(int, input().split()))

for i in range(m - 1):
    l = a[i]
    r = a[i + 1]
    if l == r:
        continue
    if l > r:
        (l, r) = (r, l)
    mdy(1, l - 1, r - l)
    mdy(l, l, r - 1)
    mdy(l + 1, r - 1, r - l - 1)
    mdy(r, r, l)
    mdy(r + 1, n, r - l)

for i in P[1:n + 1]:
    f[i] += f[i - 1]
    print(f[i], end=" ")
