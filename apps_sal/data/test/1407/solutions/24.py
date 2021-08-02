import bisect


def sieve(n):
    p = 2

    prime = [True for i in range(n + 1)]
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = []
    for p in range(2, n):
        if prime[p]:
            c.append(p)
    return c


def transpose(a, n, m):
    c = []
    for i in range(max(n, m)):
        l = []
        for j in range(max(n, m)):
            try:
                l.append(a[j][i])
            except:
                pass
        c.append(l)
    c = c[:m]
    return c


def calcost(a, c):
    cost = 0
    for i in range(len(a)):
        p = bisect.bisect_left(c, a[i])
        cost += (c[p] - a[i])
    return cost


c = sieve(1000001)
n, m = list(map(int, input().split()))
l = []
for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)
cost = []
for i in range(len(l)):
    cost.append(calcost(l[i], c))
l = transpose(l, n, m)
for i in range(len(l)):
    cost.append(calcost(l[i], c))
print(min(cost))
