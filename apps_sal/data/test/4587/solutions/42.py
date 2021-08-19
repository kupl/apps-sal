def lb(k, a):
    n = len(a)
    (l, u) = (0, n)
    while l < u:
        m = (l + u) // 2
        if k < a[m]:
            u = m
        else:
            l = m + 1
    return l


def ub(k, a):
    n = len(a)
    (l, u) = (-1, n - 1)
    while l < u:
        m = (l + u + 1) // 2
        if a[m] < k:
            l = m
        else:
            u = m - 1
    return l


N = int(input())
A = sorted([int(x) for x in input().split()])
B = sorted([int(x) for x in input().split()])
C = sorted([int(x) for x in input().split()])
res = 0
for i in range(N):
    j = ub(B[i], A)
    k = lb(B[i], C)
    res += (j + 1) * (N - k)
print(res)
