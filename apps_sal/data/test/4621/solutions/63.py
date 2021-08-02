import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def read():
    H, W = list(map(int, input().strip().split()))
    C = []
    for i in range(H):
        c = input().strip()
        C.append(c)
    return H, W, C


def solve(H, W, C):
    for c in C:
        print(c)
        print(c)


def __starting_point():
    inputs = read()
    solve(*inputs)


__starting_point()
