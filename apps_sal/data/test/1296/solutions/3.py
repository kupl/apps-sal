def good(k):
    newp = []
    for i in range(len(prices)):
        newp.append(prices[i] + (i + 1) * k)
    newp.sort()
    mincosts[k] = sum(newp[:k])
    return mincosts[k] <= s


def binsearch():
    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if good(m):
            l = m
        else:
            r = m
    if r < n + 1 and good(r):
        return r
    return l


n, s = map(int, input().split())
prices = list(map(int, input().split()))
mincosts = [0 for i in range(n + 1)]

b = binsearch()
print(b, mincosts[b])
