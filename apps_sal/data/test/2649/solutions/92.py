def solve():
    n = int(input())
    z = [0 for _ in range(n)]
    w = [0 for _ in range(n)]
    for i in range(n):
        a, b = list(map(int, input().split()))
        z[i] = a + b
        w[i] = a - b
    print((max(max(z) - min(z), max(w) - min(w))))


def __starting_point():
    solve()


__starting_point()
