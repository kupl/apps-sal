import sys
from itertools import product
input = sys.stdin.readline


def log(*args):
    print(*args, file=sys.stderr)


def main():
    n, m = map(int, input().split())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i, j, k in product([-1, 1], repeat=3):
        l2 = sorted([x * i + y * j + z * k for x, y, z in l], reverse=True)
        ans = max(ans, sum(l2[:m]))
    print(ans)


def __starting_point():
    main()


__starting_point()
