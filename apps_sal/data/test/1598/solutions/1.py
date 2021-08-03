def main():
    import sys
    input = sys.stdin.readline

    s = [int(i) for i in input()[:-1]][::-1]
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for j in range(n):
        tmp = [0, 0]
        for i in range(j, n):
            if s[i] == 0:
                tmp[0] = max(tmp) + 1
                dp[j][i] = tmp[0]
            else:
                tmp[1] += 1
                dp[j][i] = tmp[1]

    t = ""
    dp2 = [[0] * n for _ in range(n)]
    tmp = [[0, 0] for _ in range(n)]
    for j in range(n):
        okay = 1
        prev = [0] * (j + 1)
        for i in range(j + 1):
            prev[i] = tmp[i][0]
            tmp[i][0] = max(tmp[i]) + 1
            dp2[i][j] = tmp[i][0]
            if dp2[i][j] != dp[i][j]:
                okay = 0

        if not okay:
            for i in range(j + 1):
                tmp[i][0] = prev[i]
                tmp[i][1] += 1
                dp2[i][j] = tmp[i][1]
            t += '1'
        else:
            t += '0'

    print(t[::-1])

    return 0


main()
