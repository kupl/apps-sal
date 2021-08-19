import math


def solve(A: int, B: int, X: int):
    left = 1
    right = 10 ** 9
    if A + B > X:
        return 0
    if A * right + B * len(str(right)) <= X:
        return right
    while left + 1 < right:
        mid = (left + right) // 2
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid
    return left


def main():
    (A, B, X) = list(map(int, input().split()))
    ans = solve(A, B, X)
    print(ans)


def __starting_point():
    main()


__starting_point()
