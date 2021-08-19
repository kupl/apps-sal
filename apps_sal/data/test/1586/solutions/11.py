def solve(N):
    if N % 2 == 1:
        print(0)
        return
    n = 10
    ans = 0
    while n <= N:
        ans += N // n
        n *= 5
    print(ans)


def __starting_point():
    N = int(input())
    solve(N)


__starting_point()
