def main():
    MOD = 10 ** 9 + 7
    (N, K) = list(map(int, input().split()))
    ki = [[] for _ in range(N)]
    for i in range(N - 1):
        (a, b) = list(map(int, input().split()))
        ki[a - 1].append(b - 1)
        ki[b - 1].append(a - 1)
    d = [-1] * N
    que = []
    ans = K
    d[0] = 1
    for (i, nex) in enumerate(ki[0]):
        d[nex] = 1
        ans *= K - i - 1
        ans %= MOD
        que.append(nex)
    while len(que) > 0:
        now = que.pop(0)
        count = 2
        for nex in ki[now]:
            if d[nex] != -1:
                continue
            d[nex] = 1
            ans *= K - count
            count += 1
            ans %= MOD
            que.append(nex)
    print(ans)


def __starting_point():
    main()


__starting_point()
