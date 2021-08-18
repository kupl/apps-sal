def readInt():
    return int(input())


def readIntList():
    l = input()
    return list(map(int, l.split(" ")))


def build(tree, elem, v, l, r):
    if(l == r):
        tree[v] = elem[l]
    else:
        m = (l + r) // 2
        build(tree, elem, v * 2, l, m)
        build(tree, elem, v * 2 + 1, m + 1, r)
        tree[v] = max(tree[v * 2], tree[v * 2 + 1])


def find_max(tree, v, l, r, tl, tr):
    if(l > r):
        return (0, 10000)
    else:
        if(tl == l and tr == r):
            return (tree[v], tl)
        else:
            tm = (tl + tr) // 2
            m1 = find_max(tree, v * 2, l, min(r, tm), tl, tm)
            m2 = find_max(tree, v * 2 + 1, max(l, tm + 1), r, tm + 1, tr)
            if(m1[0] == m2[0]):
                if(m1[1] > m2[1]):
                    return m2
                else:
                    return m1
            else:
                if(m1[0] > m2[0]):
                    return m1
                else:
                    return m2


(n, k) = readIntList()
laws = readIntList()

tree = 4 * n * [0]

m = sum(laws[0: k])
n = len(laws)
maxs = [m]
for i in range(1, n - k + 1):
    m -= laws[i - 1]
    m += laws[i + k - 1]
    maxs.append(m)

mn = len(maxs) - 1


m1 = 0
m2 = 0


m1 = maxs[mn - k]
i1 = 0
m2 = maxs[mn]
i2 = 0

a = (mn + 1) * [0]

for i in range(mn - k, -1, -1):
    if(maxs[i + k] >= m2):
        m2 = maxs[i + k]
        i2 = i + k
    a[i] = (maxs[i] + m2, i2)


ms = 0
for i in range(0, mn - k + 1):
    if(a[i][0] > ms):
        i1 = i
        i2 = a[i][1]
        ms = a[i][0]

print(i1 + 1, i2 + 1)
