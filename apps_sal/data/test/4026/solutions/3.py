def solve():
    (n, m) = list(map(int, input().split()))
    sym = False
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        (z, w) = list(map(int, input().split()))
        if y == z:
            sym = True
    if m % 2 == 0 and sym:
        print('YES')
    else:
        print('NO')
    return


def main():
    T = int(input())
    for i in range(T):
        solve()
    return


def __starting_point():
    main()


__starting_point()
