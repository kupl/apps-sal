def main():
    from bisect import bisect_left as bl
    from itertools import accumulate as ac

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    aa = [0]+list(ac(a))
    an = aa[n]

    ok = 0
    ng = 10**10
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if sum([n-bl(a, mid-a[i]) for i in range(n)]) >= m:
            ok = mid
        else:
            ng = mid

    c = -m+sum([n-bl(a, ok-a[i]) for i in range(n)])
    ans = -c*ok
    for i in range(n):
        d = bl(a, ok-a[i])
        ans += an-aa[d]+(n-d)*a[i]
    print(ans)


main()
