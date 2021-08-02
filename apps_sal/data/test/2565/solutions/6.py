import sys

T = int(sys.stdin.readline().strip())
for t in range(0, T):
    x1, y1, z1 = list(map(int, sys.stdin.readline().strip().split()))
    x2, y2, z2 = list(map(int, sys.stdin.readline().strip().split()))
    n = x1 + y1 + z1
    print(2 * min(z1, y2) - 2 * max(0, y1 - (x2 + y2 - min(z1, y2))))
