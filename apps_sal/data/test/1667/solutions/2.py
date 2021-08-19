def union(x, y, a, each):
    x1 = x
    y1 = y
    while a[x] > 0:
        x = a[x]
    while a[y] > 0:
        y = a[y]
    each[-1 * a[x]] -= 1
    each[-1 * a[y]] -= 1
    each[-1 * (a[x] + a[y])] += 1
    if a[x] > a[y]:
        a[y] += a[x]
        a[x] = y
        res = y
    else:
        a[x] += a[y]
        a[y] = x
        res = x
    while x1 != x:
        temp = x1
        x1 = a[x1]
        a[temp] = res
    while y1 != y:
        temp = y1
        y1 = a[y1]
        a[temp] = res


def find(x, y, a):
    x1 = x
    y1 = y
    while a[x] > 0:
        x = a[x]
    while a[y] > 0:
        y = a[y]
    ans = False
    if y == x:
        ans = True
    while y1 != y:
        temp = a[y1]
        a[y1] = y
        y1 = temp
    while x1 != x:
        temp = a[x1]
        a[x1] = x
        x1 = temp
    return ans


def getsize(x, par):
    x1 = x
    while par[x] > 0:
        x = par[x]
    ans = -1 * par[x]
    while x != x1:
        temp = par[x1]
        par[x1] = x
        x1 = temp
    return ans


n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = [a[i], i]
a.sort()
par = [-2.1 for i in range(n + 1)]
max1 = 0
maxk = a[0][0] - 1
numloc = 0
each = [0 for i in range(n + 1)]
i = 0
while i < n:
    curk = a[i][0]
    while i < n and a[i][0] == curk:
        loc = a[i][1]
        if loc == 0:
            par[0] = -1
            numloc += 1
            each[1] += 1
            if par[1] != -2.1:
                numloc -= 1
                union(0, 1, par, each)
        elif loc == n - 1:
            par[n - 1] = -1
            numloc += 1
            each[1] += 1
            if par[n - 2] != -2.1:
                numloc -= 1
                union(n - 1, n - 2, par, each)
        else:
            numloc += 1
            each[1] += 1
            par[loc] = -1
            if par[loc - 1] != -2.1:
                union(loc, loc - 1, par, each)
                numloc -= 1
            if par[loc + 1] != -2.1:
                union(loc, loc + 1, par, each)
                numloc -= 1
        i += 1
    if each[getsize(loc, par)] == numloc:
        if numloc > max1:
            maxk = curk
            max1 = numloc
print(maxk + 1)
