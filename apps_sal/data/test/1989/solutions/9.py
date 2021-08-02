def merge(a, x, y, u, v):
    i = 0
    b = a[x:v + 1]
    j = u
    for k in range(x, y + 1):
        while j <= v and a[j] < a[k]:
            b[i] = a[j]
            j += 1
            i += 1
        b[i] = a[k]
        i += 1
    while j <= u:
        b[i] = a[j]
        i += 1
        j += 1
    return b


def cal(l, r, x, y):
    if x == y:
        return 0
    mid = (x + y) // 2
    res = cal(l, r, x, mid) + cal(l, r, mid + 1, y)

    j = mid + 1
    for i in range(x, mid + 1):
        while j <= y and r[j] < l[i]:
            j += 1
        res += j - mid - 1
    l[x:y + 1] = merge(l, x, mid, mid + 1, y)
    r[x:y + 1] = merge(r, x, mid, mid + 1, y)
    return res


def countOccurrencePairs(a):
    n = len(a)
    l = [0 for _ in range(n)]
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
        l[i] = d[a[i]]

    r = [0 for _ in range(n)]
    d = {}
    for i in range(n - 1, -1, -1):
        if a[i] not in d:
            d[a[i]] = 0
        d[a[i]] += 1
        r[i] = d[a[i]]

    return cal(l, r, 0, n - 1)


n = int(input())
a = list(map(int, input().split()))
print(countOccurrencePairs(a))
