
def get_ans(n, p, q, r, a):
    maxpre = [-100000000] * n
    minpre = [100000000] * n
    maxsuf = [-100000000] * n
    minsuf = [100000000] * n

    curmax = a[0]
    curmin = a[0]

    for i in range(n):
        if a[i] > curmax:
            curmax = a[i]
        maxpre[i] = curmax

        if a[i] < curmin:
            curmin = a[i]
        minpre[i] = curmin

    curmax = a[n - 1]
    curmin = a[n - 1]

    for i in range(n - 1, -1, -1):
        if a[i] > curmax:
            curmax = a[i]
        maxsuf[i] = curmax

        if a[i] < curmin:
            curmin = a[i]
        minsuf[i] = curmin

    ans = []
    for i in range(n):
        pmas = maxpre if p > 0 else minpre
        rmas = maxsuf if r > 0 else minsuf

        ans.append(pmas[i] * p + a[i] * q + rmas[i] * r)

    return max(ans)


n, p, q, r = tuple(map(int, input().split()))
a = list(map(int, input().split()))
print(get_ans(n, p, q, r, a))
