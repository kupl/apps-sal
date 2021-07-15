def main():
    n = int(input())
    a = list(map(int, input().split()))
    xor = 0
    for i in range(2, n):
        xor ^= a[i]
    s = a[0] + a[1]
    dp = [[[-1 for k in range(2)] for j in range(2)] for i in range(45)]
    p = a[0]
    dp[0][0][0] = 0
    for i in range(44):
        crrx = xor&1
        crrs = s&1
        crrp = p&1
        for j in range(2):
            for k in range(2):
                if dp[i][j][k] == -1:
                    continue
                for nxtp in range(2):
                    for nxtq in range(2):
                        nxti = i+1
                        nxtj = 0
                        nxtk = k
                        if (nxtp ^ nxtq) != crrx:
                            continue
                        nxts = nxtp+nxtq+j
                        if nxts%2 != crrs:
                            continue
                        if nxts >= 2:
                            nxtj = 1
                        if crrp < nxtp:
                            nxtk = 1
                        elif crrp == nxtp:
                            nxtk = k
                        else:
                            nxtk = 0
                        dp[nxti][nxtj][nxtk] = max(dp[nxti][nxtj][nxtk], dp[i][j][k]+(1<<i)*nxtp)
        xor //= 2
        s //= 2
        p //= 2
    if dp[-1][0][0] > 0:
        print(a[0] - dp[-1][0][0])
    else:
        print(-1)

def __starting_point():
    main()
__starting_point()
