def solve():
    size = int(input())
    ls = list(map(int, input().rstrip().split()))
    dp0 = [1 for i in range(size)]
    dp1 = [1 for i in range(size)]
    for i in range(1, size):
        dp0[i] = dp0[i - 1] + 1 if ls[i - 1] < ls[i] else 1
    for i in range(0, size - 1)[::-1]:
        dp1[i] = dp1[i + 1] + 1 if ls[i + 1] > ls[i] else 1
    best = max(max(dp0), max(dp1))
    for i in range(0, size):
        if i >= 1:
            best = max(best, dp0[i - 1] + 1)
        if i <= size - 2:
            best = max(best, dp1[i + 1] + 1)
        if i <= size - 2 and i >= 1:
            if ls[i - 1] + 1 < ls[i + 1]:
                best = max(best, dp0[i - 1] + dp1[i + 1] + 1)
    return best


def __starting_point():
    print(solve())


__starting_point()
