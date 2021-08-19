from sys import stdin


def solve():
    #stdin = open("C.txt")

    a = stdin.readline().strip()
    b = stdin.readline().strip()

    n = len(a)
    m = len(b)

    a_cnt = a[:m].count("1")
    b_cnt = b.count("1")

    ans = 0

    if (a_cnt + b_cnt) % 2 == 0:
        ans = 1

    for i in range(1, n - m + 1):
        if a[i - 1] == "1":
            a_cnt -= 1

        if a[i + m - 1] == "1":
            a_cnt += 1

        if (a_cnt + b_cnt) % 2 == 0:
            ans += 1

    print(ans)


def __starting_point():
    solve()


__starting_point()
