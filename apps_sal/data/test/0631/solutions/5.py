def solve():
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) == m:
        print('YES')
    else:
        print('NO')


def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
