def resolve():
    import sys

    readline = sys.stdin.readline

    N = int(readline())

    red = [list(map(int, readline().split())) for _ in [0] * N]
    blue = [list(map(int, readline().split())) for _ in [0] * N]

    red.sort(key=lambda x: x[1], reverse=True)
    blue.sort()

    ans = 0
    for c, d in blue:
        for a, b in red:
            if a <= c and b <= d:
                ans += 1
                red.remove([a, b])
                break
    print(ans)


resolve()
