#!/usr/bin/env python3


def main():
    try:
        while True:
            n = int(input())
            left = [0] * n
            right = [0] * n
            for i in range(n):
                left[i], right[i] = list(map(int, input().split()))
            ls = sum(left)
            rs = sum(right)
            best = abs(ls - rs)
            result = -1
            for i, (cl, cr) in enumerate(zip(left, right)):
                cur = abs((ls - cl + cr) - (rs - cr + cl))
                if cur > best:
                    best = cur
                    result = i

            print(result + 1)

    except EOFError:
        pass


main()

