import collections as co


def searchRoot(n):
    par = parList[n]
    if n == par:
        if len(q) > 0:
            rootIn(q, n)
        return n
    else:
        q.append(n)
        return(searchRoot(par))


def rootIn(q, root):
    while len(q) > 0:
        parList[q.popleft()] = root


def UnionFind(n, m, lis):
    for i in range(m):
        a, b = lis[i]
        aRoot = searchRoot(a)
        bRoot = searchRoot(b)
        if aRoot != bRoot:
            parList[max(aRoot, bRoot)] = min(aRoot, bRoot)

    ansDic = dict()
    rootSet = set()
    for i in range(0, n):
        root = searchRoot(i)
        if root in rootSet:
            ansDic[root] += 1
        else:
            rootSet.add(root)
            ansDic[root] = 1

    return ansDic


n, k = list(map(int, input().split()))

a = []
for i in range(n):
    aRow = list(map(int, input().split()))
    a.append(aRow)

rowLis = []
for i in range(n - 1):
    for j in range(i + 1, n):
        check = True
        for l in range(n):
            if a[i][l] + a[j][l] > k:
                check = False
                break
        if check:
            rowLis.append([i, j])
parList = [i for i in range(n + 1)]
q = co.deque()
rowDic = UnionFind(n, len(rowLis), rowLis)


colLis = []
for i in range(n - 1):
    for j in range(i + 1, n):
        check = True
        for l in range(n):
            if a[l][i] + a[l][j] > k:
                check = False
                break
        if check:
            colLis.append([i, j])
parList = [i for i in range(n + 1)]
q = co.deque()
colDic = UnionFind(n, len(colLis), colLis)

ans = 1
for i in rowDic.values():
    for j in range(1, i + 1):
        ans = ans * j
for i in colDic.values():
    for j in range(1, i + 1):
        ans = ans * j

ans = ans % 998244353
print(ans)
