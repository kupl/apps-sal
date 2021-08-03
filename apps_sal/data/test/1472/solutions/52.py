from collections import defaultdict
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    dis = defaultdict(int)
    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            d = min(abs(i2 - i1), abs(x - i1) + abs(y - i2) + 1, abs(x - i2) + abs(y - i1) + 1)
            dis[d] += 1

    for k1 in range(1, n):
        print(dis[k1])


def __starting_point():
    main()


__starting_point()
