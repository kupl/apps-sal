for _ in range(int(input())):
    (n, x, y) = map(int, input().split())
    ans = [0] * n
    mn = 9999999999999999999999999
    for i in range(n - 1):
        res = [0] * n
        res[i] = x
        for j in range(i + 1, n):
            if (y - x) % (j - i) == 0:
                res[j] = y
                ok = 1
                f = (y - x) // (j - i)
                for ii in range(i - 1, -1, -1):
                    res[ii] = res[ii + 1] - f
                for jj in range(i + 1, n):
                    res[jj] = res[jj - 1] + f
                if res[-1] < mn and res[0] > 0:
                    mn = res[-1]
                    ans = res
    print(*ans)
