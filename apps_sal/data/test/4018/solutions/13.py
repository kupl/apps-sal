def super_solve(n, k, s):
    last = []
    for i in range(0, 256):
        last.append(0)
    dp = []
    for i in range(0, 105):
        tmp = []
        for j in range(0, 105):
            tmp.append(0)
        dp.append(tmp)
    now = []
    for i in range(0, 105):
        tmp = []
        for j in range(0, 105):
            tmp.append(0)
        now.append(tmp)
    dp[0][0] = 1
    now[0][0] = 1
    for i in range(1, n + 1):
        c = ord(s[i])
        for j in range(0, n + 1):
            dp[i][j] += dp[i - 1][j]
        for j in range(1, n + 1):
            dp[i][j] += dp[i - 1][j - 1]
        if last[c] > 0:
            for j in range(1, n + 1):
                dp[i][j] -= dp[last[c] - 1][j - 1]
        for j in range(0, n + 1):
            now[i][j] = dp[i][j] - dp[i - 1][j]
        last[c] = i
    cost = 0
    baki = k
    j = n
    while j >= 0:
        for i in range(0, n + 1):
            cur = now[i][j]
            my = min(baki, cur)
            cost += my * j
            baki -= my
        j -= 1
    ret = k * n - cost
    if baki > 0:
        ret = -1
    return ret


def main():
    line = input()
    line = line.split(' ')
    n = int(line[0])
    k = int(line[1])
    tmp = input()
    s = []
    s.append(0)
    for i in range(0, n):
        s.append(tmp[i])
    ret = super_solve(n, k, s)
    print(ret)


def __starting_point():
    main()


__starting_point()
