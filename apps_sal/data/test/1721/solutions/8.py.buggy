def build(v, l, r):
    nonlocal tree
    if r - l == 1:
        tree[v] = u[l]
    else:
        m = (l + r) // 2
        build(2 * v + 1, l, m)
        build(2 * v + 2, m, r)
        tree[v] = tree[2 * v + 1] + tree[2 * v + 2]


def rsq(v, l, r, a, b):
    nonlocal tree
    if l >= b or a >= r:
        return 0
    if l >= a and r <= b:
        return tree[v]
    m = (l + r) // 2
    return rsq(2 * v + 1, l, m, a, b) + \
        rsq(2 * v + 2, m, r, a, b)


def update(v, l, r, i, x):
    nonlocal tree
    if i < l or i >= r:
        return
    if r - l == 1:
        tree[v] = x
    else:
        m = (l + r) // 2
        update(2 * v + 1, l, m, i, x)
        update(2 * v + 2, m, r, i, x)
        tree[v] = tree[2 * v + 1] + tree[2 * v + 2]


n = int(input())
a = list(input())
sz = 1
while sz < n:
    sz *= 2
tree = [0] * (2 * sz - 1)
u = [0] * n
while len(u) < sz:
    u.append(0)
build(0, 0, sz)
ss = []
for i in range(26):
    ss.append([])
for i in range(n):
    a[i] = ord(a[i]) - ord('a')
    ss[a[i]].append(i)
a.reverse()
ans = 0
for i in range(n - 1, -1, -1):
    L, R = ss[a[i]][-1], i
    ans += R - L + rsq(0, 0, sz, 0, L)
    update(0, 0, sz, L, 1)
    ss[a[i]].pop()
print(ans)
