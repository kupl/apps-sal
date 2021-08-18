def solve(N, K, td):
    max_t = [0] * (N + 1)
    for i in range(N):
        if max_t[td[i][0]] < td[i][1]:
            max_t[td[i][0]], td[i][1] = td[i][1], max_t[td[i][0]]
    d = [tdi[1] for tdi in td]
    max_t.sort(reverse=True)
    d.sort(reverse=True)
    c_sum_max_t = [0]
    for i in range(N + 1):
        c_sum_max_t.append(c_sum_max_t[-1] + max_t[i])
    c_sum_d = [0]
    for i in range(N):
        c_sum_d.append(c_sum_d[-1] + d[i])
    ans = 0
    kind = len([i for i in max_t if i > 0])
    for i in range(1, min(kind + 1, K + 1)):
        ans = max(c_sum_max_t[i] + c_sum_d[K - i] + i ** 2, ans)
    print(ans)


def __starting_point():
    N, K = list(map(int, input().split()))
    td = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, td)


__starting_point()
