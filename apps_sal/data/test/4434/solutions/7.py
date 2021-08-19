def solve():
    n = int(input())
    iters = n // 2
    out = 0
    for i in range(iters + 1):
        out += 8 * i * i
    print(out)


def __starting_point():
    t = int(input())
    for tc in range(t):
        solve()


__starting_point()
