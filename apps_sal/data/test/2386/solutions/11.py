def snk(b, A):
    res = 0
    for i in range(N):
        res += abs(A[i] - (b + i + 1))
    return res


N = int(input())
A = [int(i) for i in input().split()]
l = 1 - N
r = 10 ** 9 + N
while r - l > 2:
    ls = snk(l, A)
    rs = snk(r - 1, A)
    m = (l + r) // 2
    ms = snk(m, A)
    mp1s = snk(m + 1, A)
    mm1s = snk(m - 1, A)
    if mp1s <= ms <= mm1s:
        l = m
    elif mp1s >= ms >= mm1s:
        r = m + 1
    elif mp1s >= ms and ms <= mm1s:
        break
print(ms)
