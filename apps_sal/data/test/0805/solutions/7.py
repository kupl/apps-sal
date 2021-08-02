import sys; sys.setrecursionlimit(1000000)


def solve():
    n, = rv()
    count = [0] * 100
    leftmost, rightmost, = rv()
    for seg in range(n - 1):
        left, right, = rv()
        for val in range(left, right):
            count[val] += 1
    res = 0
    for val in range(leftmost, rightmost):
        if count[val] == 0: res += 1
    print(res)


def rv(): return list(map(int, input().split()))
def rl(n): return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544: sys.stdin = open("test.txt")
solve()
