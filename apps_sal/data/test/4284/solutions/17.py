import sys
input = sys.stdin.readline

Q = int(input())
for testcase in range(Q):
    k, n, a, b = list(map(int, input().split()))

    if k <= n * b:
        print(-1)
        continue

    print(min(n, (k - n * b - 1) // (a - b)))
