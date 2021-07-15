for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    allCnts = []
    for k in range(n+m-1):
        cnt = [0,0]
        i = k+1
        for j in range(n+m):
            i -= 1
            if i < 0 or i >= n or j >= m:
                continue
            cnt[a[i][j]] += 1
        allCnts.append(cnt)
    for i in range(len(allCnts) // 2):
        zeros = allCnts[i][0] + allCnts[-i-1][0]
        ones = allCnts[i][1] + allCnts[-i-1][1]
        ans += min(zeros, ones)
    print(ans)

