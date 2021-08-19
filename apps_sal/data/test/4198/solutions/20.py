#!/usr/bin/env python3
def main():
    A, B, X = list(map(int, input().split()))
    num_max = 10 ** 9
    digit_max = len(str(num_max))

    ans = 0
    for n in range(1, digit_max + 1):
        res = (X - B * n) // A
        if res > num_max:
            res = num_max
        if res < 0:
            continue
        digit = len(str(res))
        if digit == n:
            ans = max(ans, res)
        if digit > n:
            ans = max(ans, 10 ** n - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
