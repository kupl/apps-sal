def main():
    n, c = map(int, input().split())
    sushi = [None] * n
    for i in range(n):
        sushi[i] = list(map(int, input().split()))
    cal_r = [None] * n
    cal_l = [None] * n
    max_r = [None] * n
    max_l = [None] * n
    cal_r[0] = sushi[0][1] - sushi[0][0]
    max_r[0] = cal_r[0]
    for i in range(1, n):
        cal_r[i] = cal_r[i - 1] + sushi[i][1] - (sushi[i][0] - sushi[i - 1][0])
        max_r[i] = max(max_r[i - 1], cal_r[i])
    cal_l[n - 1] = sushi[n - 1][1] - (c - sushi[n - 1][0])
    max_l[n - 1] = cal_l[n - 1]
    for i in reversed(range(n - 1)):
        cal_l[i] = cal_l[i + 1] + sushi[i][1] - (sushi[i + 1][0] - sushi[i][0])
        max_l[i] = max(max_l[i + 1], cal_l[i])
    max_r_1 = max(max_r)
    max_l_1 = max(max_l)
    ans = max(0, max_r_1, max_l_1)
    cal_r_2 = [None] * n
    cal_l_2 = [None] * n
    cal_r_2[n - 1] = 0
    cal_l_2[0] = 0
    for i in range(n - 1):
        cal_r_2[i] = cal_r[i] - sushi[i][0] + max_l[i + 1]
    for i in reversed(range(1, n)):
        cal_l_2[i] = cal_l[i] - (c - sushi[i][0]) + max_r[i - 1]
    max_r_2 = max(cal_r_2)
    max_l_2 = max(cal_l_2)
    ans = max(ans, max_l_2, max_r_2)
    print(ans)


def __starting_point():
    main()


__starting_point()
