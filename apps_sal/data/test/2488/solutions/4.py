import bisect


def main():
    (N, D, A) = list(map(int, input().split()))
    monsters = [list(map(int, input().split())) for _ in range(N)]
    monsters.sort()
    X = [m[0] for m in monsters]
    ans = 0
    damages = [0] * (N + 1)
    for (n, monster) in enumerate(monsters):
        (x, h) = monster
        h = max(0, h - damages[n])
        to_n = bisect.bisect_right(X, x + 2 * D)
        cnt = (h + A - 1) // A
        ans += cnt
        damages[n] += A * cnt
        damages[to_n] -= A * cnt
        damages[n + 1] += damages[n]
    print(ans)


def __starting_point():
    main()


__starting_point()
