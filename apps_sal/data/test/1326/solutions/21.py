import sys
import math

input = sys.stdin.readline


def main():

    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        num = N // i
        ans += num * (num + 1) // 2 * i

    print(ans)


def __starting_point():
    main()


__starting_point()
