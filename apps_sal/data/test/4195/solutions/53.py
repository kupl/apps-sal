def solve(D, N):
    if N < 100:
        ans = 100 ** D * N
    else:
        ans = 100 ** D * 101
    return ans


def __starting_point():
    (D, N) = list(map(int, input().split()))
    print(solve(D, N))


__starting_point()
