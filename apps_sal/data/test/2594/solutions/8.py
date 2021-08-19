import sys
max_int = 1000000001  # 10^9+1
min_int = -max_int

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().split()))
    print((n * m + 1) // 2)
