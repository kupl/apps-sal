def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    res1 = [0 for i in range(n)]
    maxes = a[:]
    maxes.sort()
    for i in range(n):
        res1[i] = (a[i] + 1) // 2
    w -= sum(res1)
    if w < 0:
        print(-1)
        return
    i = -1
    while w > 0:
        maxi = a.index(maxes[i])
        if w > a[maxi] - res1[maxi]:
            w -= (a[maxi] - res1[maxi])
            res1[maxi] = a[maxi]
            a[maxi] = 0
            maxes[i] = 0
        else:
            res1[maxi] += w
            w = 0
        i -= 1
    print(*res1)


main()
