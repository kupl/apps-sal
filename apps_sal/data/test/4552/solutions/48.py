def solve():
    n = int(input())
    oc = [list(map(int, input().split())) for _ in range(n)]
    prof = [list(map(int, input().split())) for _ in range(n)]
    ans = -9999999999
    for a in range(1, 1 << 10):
        res = 0
        for i in range(n):
            cnt = 0
            for x in range(10):
                if (a >> x) % 2 == 1 and oc[i][x] == 1:
                    cnt += 1
            res += prof[i][cnt]
        ans = max(ans, res)
    print(ans)


solve()
