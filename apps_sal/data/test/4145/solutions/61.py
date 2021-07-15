#!/usr/bin/env python3
def solve(x: int):
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            return False
    return True


def main():
    X = int(input())

    while True:
        if solve(X):
            print(X)
            break
        else:
            X += 1


def __starting_point():
    main()

__starting_point()
