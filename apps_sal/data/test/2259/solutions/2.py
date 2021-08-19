import sys
sys.setrecursionlimit(1000000)


def solve():
    (n,) = rv()
    (a,) = rl(1)
    mem = [10000000] * (n + 1)
    mem[0] = a[0]
    for i in range(1, n):
        (left, right) = (0, n - 1)
        while left < right:
            mid = (left + right) // 2
            if a[i] < mem[mid]:
                right = mid
            else:
                left = mid + 1
        mem[left] = a[i]
    res = 0
    for i in range(1, n):
        if mem[i] != 10000000:
            res = i
    print(res + 1)


def rv():
    return list(map(int, input().split()))


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
