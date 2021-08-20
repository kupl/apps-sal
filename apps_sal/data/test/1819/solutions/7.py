import sys
T = int(sys.stdin.readline().strip())
for t in range(0, T):
    (n, x) = list(map(int, sys.stdin.readline().strip().split()))
    print(2 * x)
