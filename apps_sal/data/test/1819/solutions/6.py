import sys
sys.setrecursionlimit(10**9)

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    # 2, 4, 6, ...
    print(2 * x)
