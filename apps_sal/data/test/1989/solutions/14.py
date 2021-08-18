n = int(input())


def getsum(BITTree, i):
    s = 0

    i = i + 1

    while i > 0:

        s += BITTree[i]

        i -= i & (-i)
    return s


def updatebit(BITTree, n, i, v):

    i += 1

    while i <= n:

        BITTree[i] += v

        i += i & (-i)


a = list(map(int, input().split()))
pre = dict()
pos = dict()
for i in range(n):
    if(pre.get(a[i], None) == None):
        pre[a[i]] = 0
    pre[a[i]] += 1
ans = 0
BIT = [0] * (n + 1)
for i in range(n - 1, 0, -1):
    pre[a[i]] -= 1
    if(pos.get(a[i], None) == None):
        pos[a[i]] = 0
    pos[a[i]] += 1
    updatebit(BIT, n, pos[a[i]], 1)
    temp = getsum(BIT, pre[a[i - 1]] - 1)
    ans += temp
print(ans)
