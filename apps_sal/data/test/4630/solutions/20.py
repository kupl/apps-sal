import sys


def main():
    for tc in range(int(input())):
        n = int(input())
        arr = get_array()
        for i in range(n):
            arr[i] -= 1
        ans = [1] * n
        d = {}
        for i in range(n):
            if i in d:
                continue
            tmp = {}
            j = arr[i]
            while j != i:
                ans[i] += 1
                j = arr[j]
                tmp[arr[j]] = 1
            for j in tmp:
                ans[j] = ans[i]
                d[j] = 1
        print(*ans)


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
