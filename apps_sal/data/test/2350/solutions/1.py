import sys
input = sys.stdin.readline
for f in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print((x2 - x1) * (y2 - y1) + 1)
