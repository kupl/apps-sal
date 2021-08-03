def solve():
    n, m = list(map(int, input().split()))
    if n not in (m, m + 1):
        return 3
    l = [0] * (n + 1)
    for _ in range(m):
        x, y = list(map(int, input().split()))
        l[x] += 1
        l[y] += 1
    c2 = l.count(2)
    if m == n == c2:
        return 1
    if m == n - 1:
        c1 = l.count(1)
        if c1 == 2 and c2 == n - 2:
            return 0
        if c1 == m and m in l:
            return 2
    return 3


def main():
    print(("bus", "ring", "star", "unknown")[solve()], "topology")


def __starting_point():
    main()


__starting_point()
