N = int(input())


def solve_function(N):
    if N % 2 == 1:
        return 0

    n = 10
    ans = 0
    while True:
        if n > N:
            break
        ans += N // n
        n *= 5
    return ans


if solve_function(N):
    print(solve_function(N))
else:
    print(0)
