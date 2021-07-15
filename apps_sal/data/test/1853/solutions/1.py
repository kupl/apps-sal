def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

# D. Similar Arrays

n, m = mi()
g = [[] for i in range(n + 1)]
e = []
for i in range(m):
    a, b = mi()
    e.append((a, b))
    g[a].append(b)
    g[b].append(a)

eq = None
if n > 1:
    for i in range(1, n + 1):
        if len(g[i]) == n - 1:
            continue
        s = set(g[i])
        for j in range(1, n + 1):
            if i != j and j not in s:
                eq = i, j
                break
        if eq: break

if eq:
    a, b = [0] * n, [0] * n
    a[eq[0] - 1] = 1
    a[eq[1] - 1] = 2
    b[eq[0] - 1] = b[eq[1] - 1] = 1
    c = 3
    for i in range(n):
        if not a[i]:
            a[i] = b[i] = c
            c += 1
    for i, j in e:
        if (a[i - 1] < a[j - 1]) != (b[i - 1] < b[j - 1]):
            eq = None
            break

if eq:
    print('YES')
    print(*a)
    print(*b)
else:
    print('NO')

