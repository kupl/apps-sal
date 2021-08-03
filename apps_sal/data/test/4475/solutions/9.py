import sys
input = sys.stdin.readline


def fmin(a, b, x, y, n):
    v = max(a - n, x)
    val = n - (a - v)
    v1 = max(b - val, y)
    return v * v1


T = int(input())
for _ in range(T):
    a, b, x, y, n = list(map(int, input().split()))
    v = min(fmin(a, b, x, y, n), fmin(b, a, y, x, n))
    print(v)
