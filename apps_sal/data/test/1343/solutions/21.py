(n, m, k) = list(map(int, input().split()))
uvl = [list(map(int, input().split())) for i in range(m)]
if k == 0:
    print('-1')
else:
    ai = list(map(int, input().split()))
    ai.sort()
    ans = 1000000001

    def bf(x):
        l = 0
        r = k - 1
        while l < r:
            mid = (l + r) // 2
            if ai[mid] < x:
                l = mid + 1
            else:
                r = mid
        if ai[r] == x:
            return 1
        else:
            return 0
    for i in range(m):
        if bf(uvl[i][0]) != bf(uvl[i][1]):
            ans = min(ans, uvl[i][2])
    if ans == 1000000001:
        print('-1')
    else:
        print(ans)
