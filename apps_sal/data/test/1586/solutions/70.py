N = int(input())


def solve_function(N):
    if N % 2 == 1:
        return 0

    it_can_be_divisible = 10
    ans = 0
    while True:
        if it_can_be_divisible > N:
            break
        ans += N // it_can_be_divisible
        it_can_be_divisible *= 5

    return ans


if solve_function(N):
    print(solve_function(N))
else:
    print(0)
