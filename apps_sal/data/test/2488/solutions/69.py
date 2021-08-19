def resolve():
    (N, D, A) = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    imos = [0] * (N + 1)
    ans = 0
    R = 0
    for l in range(N):
        if l:
            imos[l] += imos[l - 1]
        x = AB[l][0]
        h = AB[l][1]
        if imos[l] < h:
            R = max(R, l + 1)
            while R < N and AB[R][0] <= 2 * D + x:
                R += 1
            d = h - imos[l]
            cnt = (d + A - 1) // A
            imos[l] += cnt * A
            imos[R] -= cnt * A
            ans += cnt
    print(ans)


def __starting_point():
    resolve()


__starting_point()
