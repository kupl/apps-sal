def solve():
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in a[1:]:
        ans += (k - i) // a[0]
    print(ans)
    return


def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
