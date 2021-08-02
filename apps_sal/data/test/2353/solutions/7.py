import sys
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
input = sys.stdin.readline


T = int(input())

for t in range(T):
    a, b, c, d = list(map(int, input().split()))

    if a <= b:
        print(b)
    else:
        if c <= d:
            print(-1)
        else:
            cnt = (a - b - 1) // (c - d) + 1
            print(b + cnt * c)
