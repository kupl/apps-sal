import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, r = list(map(int, input().split()))

    if r >= n:
        print((n - 1) * n // 2 + 1)
    else:
        print(r * (r + 1) // 2)
