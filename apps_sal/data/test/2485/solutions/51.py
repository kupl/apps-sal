import sys


def solve():
    readline = sys.stdin.readline
    (H, W, M) = map(int, readline().split())
    h = [0] * H
    w = [0] * W
    b = set()
    for _ in range(M):
        (y, x) = map(int, readline().split())
        x -= 1
        y -= 1
        h[y] += 1
        w[x] += 1
        b.add(y * W + x)
    h = sorted(zip(h, range(H)), reverse=True)
    ans = 0
    for i in range(W):
        x = w[i]
        for (y, j) in h:
            if x + y > ans:
                if j * W + i in b:
                    ans = x + y - 1
                else:
                    ans = x + y
                    break
            else:
                break
    print(ans)


def __starting_point():
    solve()


__starting_point()
