

import sys


def main():
    for tc in range(int(input())):
        n = int(input())
        arr = get_array()
        ans = [1] * n
        for i in range(n):
            j = arr[i] - 1
            while j != i:
                ans[i] += 1
                j = arr[j] - 1
        print(*ans)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
