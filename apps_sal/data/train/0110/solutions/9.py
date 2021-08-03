import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    peak = [0] + [1 if a[i - 1] < a[i] and a[i] > a[i + 1] else 0 for i in range(1, n - 1)] + [0]
    b = [None] * (n - k + 1)
    b[0] = sum(peak[1: k - 1])
    for i in range(1, n - k + 1):
        b[i] = b[i - 1] - peak[i] + peak[i + k - 2]
    p = max(b)
    print(p + 1, b.index(p) + 1)
