import sys
(r, c) = map(int, input().split())
m = []
p = [i for i in range(0, r + c)]
tree = [[] for i in range(0, r + c)]
for i in range(0, r):
    s = input().split('\n')[0]
    m.append(list(s))


def find(i):
    if p[i] == i:
        return i
    par = find(p[i])
    p[i] = par
    return p[i]


def join(i, j):
    p[find(i)] = find(j)


for i in range(0, r):
    for j in range(0, c):
        if m[i][j] == '=':
            join(i, r + j)
        elif m[i][j] == '>':
            tree[i].append(r + j)
        elif m[i][j] == '<':
            tree[r + j].append(i)
v = [False for i in range(0, r + c)]
v2 = [False for i in range(0, r + c)]
a = [1 for i in range(0, r + c)]
l = [[] for i in range(0, r + c)]
for i in range(0, r + c):
    l[find(i)].append(i)


def dfs(i):
    i = find(i)
    if v[i]:
        return sys.maxsize
    elif v2[i]:
        return a[i]
    v[i] = True
    for k in l[i]:
        for j in tree[k]:
            a[i] = max(dfs(j) + 1, a[i])
    v[i] = False
    v2[i] = True
    return a[i]


A = []
ans = True
for i in range(0, r + c):
    A.append(dfs(i))
    if A[i] > r + c:
        ans = False
m = {}
index = 0
pre = -1
for i in sorted(A):
    if pre == i:
        m[i] = index
    else:
        pre = i
        index += 1
        m[i] = index
for i in range(0, r + c):
    A[i] = m[A[i]]
if ans:
    print('Yes')
    print(str(A[:r]).replace(',', '').replace('[', '').replace(']', ''))
    print(str(A[r:]).replace(',', '').replace('[', '').replace(']', ''))
else:
    print('No')
