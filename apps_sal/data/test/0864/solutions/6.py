import sys
import os


def test(food, n, day):
    p = 0
    for i in food:
        p += i // day
    return p >= n


def solve(package, n):
    food = dict()
    for f in package:
        if f in food:
            food[f] += 1
        else:
            food[f] = 1
    r = list(food.values())
    left = 0
    right = 1000
    while right > left + 1:
        mid = (left + right) // 2
        if test(r, n, mid):
            left = mid
        else:
            right = mid
    return left


def main():
    (n, m) = map(int, input().split())
    package = list(map(int, input().split()))
    print(solve(package, n))


def __starting_point():
    main()


__starting_point()
