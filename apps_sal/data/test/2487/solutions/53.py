def main():
    N = int(input())
    uv = [list(map(int, input().split())) for _ in range(N - 1)]
    ans = 0
    for i in range(N):
        ans += (i + 1) * (N - i)
    for (u, v) in uv:
        ans -= min(u, v) * (N - max(u, v) + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
