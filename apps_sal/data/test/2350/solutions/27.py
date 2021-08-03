import sys
input = sys.stdin.readline
for nt in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = x2 - x1
    m = y2 - y1
    print(n * m + 1)
