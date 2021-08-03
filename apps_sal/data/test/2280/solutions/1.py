import sys

T = int(sys.stdin.readline().strip())
for t in range(0, T):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    print(min([len(a) - 2, a[-2] - 1]))
