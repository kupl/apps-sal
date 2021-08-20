import sys


def main():
    from collections import Counter
    from operator import itemgetter
    for tc in range(int(input())):
        n = int(input())
        arr = get_array()
        if n < 2:
            print(-1)
            continue
        d = {}
        ans = 10 ** 9
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]] = i
            else:
                ans = min(ans, i - d[arr[i]] + 1)
                d[arr[i]] = i
        if ans == 10 ** 9:
            ans = -1
        print(ans)


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
