def solve():
    N = int(input())
    cnt = [[0] * 10 for i in range(10)]
    for i in range(1, N + 1):
        target_str = str(i)
        cnt[int(target_str[0])][int(target_str[-1])] += 1
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += cnt[i][j] * cnt[j][i]
    print(ans)


def __starting_point():
    solve()


__starting_point()
