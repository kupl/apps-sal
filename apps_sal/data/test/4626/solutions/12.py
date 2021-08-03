import sys

q = int(sys.stdin.readline())


def dist(x, y, z):
    return abs(x - y) + abs(x - z) + abs(y - z)


def solve(a, b, c):
    best_dist = 10**18
    for ax in [-1, 0, 1]:
        for bx in [-1, 0, 1]:
            for cx in [-1, 0, 1]:
                best_dist = min(best_dist, dist(a + ax, b + bx, c + cx))
    return best_dist


for _ in range(q):
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))
    print(solve(a, b, c))
