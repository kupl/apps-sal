import sys


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = get_array()
        d = {}

        def solve(i):
            idx = 0
            for j in range(n):
                if arr[j] == i:
                    idx = j
                    break
            p = idx
            for j in range(idx - 1, -1, -1):
                if p in d:
                    break
                if arr[j] < arr[p]:
                    break
                (arr[p], arr[j]) = (arr[j], arr[p])
                d[p] = 1
                p -= 1
        for i in range(1, n + 1):
            solve(i)
        print(*arr)


def input():
    return sys.stdin.readline().strip()


def get_ints():
    return list(map(int, input().split()))


def get_array():
    return list(map(int, input().split()))


main()
