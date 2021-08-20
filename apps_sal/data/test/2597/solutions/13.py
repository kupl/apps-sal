for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort(reverse=1)

    def check(mi):
        return l[mi] >= mi + 1
    lo = 0
    hi = n - 1
    while lo <= hi:
        mi = lo + hi >> 1
        if check(mi):
            ans = mi + 1
            lo = mi + 1
        else:
            hi = mi - 1
    print(ans)
