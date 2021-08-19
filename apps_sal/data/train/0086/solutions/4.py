import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    ZERO = A.count(0)
    if ZERO >= n // 2:
        print(ZERO)
        print(*[0] * ZERO)
    else:
        ONE = n - ZERO
        print(ONE // 2 * 2)
        print(*[1] * (ONE // 2 * 2))
