import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, m, k in Query:
    p = n // k
    if p >= m:
        ans = m
    else:
        ans = max(p - (m - p + k - 2) // (k - 1), 0)
    print(ans)
