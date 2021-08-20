def solve():
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) == m:
        print('YES')
    else:
        print('NO')
    return


def main():
    t = int(input())
    for i in range(t):
        solve()
    return


def __starting_point():
    main()


__starting_point()
