def f(n):
    minn = 0
    maxx = 30
    mid = 10
    while mid != minn:
        if n // 2 ** mid == n / 2 ** mid:
            minn = mid
            mid = (minn + maxx) // 2
        else:
            maxx = mid
            mid = (minn + maxx) // 2
    return mid


t = int(input())
for i in range(t):
    d = dict()
    n = int(input())
    a = set(map(int, input().split()))
    for j in a:
        p = f(j)
        if j // 2 ** p in d:
            if p > d[j // 2 ** p]:
                d[j // 2 ** p] = p
        else:
            d[j // 2 ** p] = p
    print(sum(d.values()))
