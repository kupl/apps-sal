from math import ceil
t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    a = min(n // k, m)
    print(a - ceil((m - a) / (k - 1)))
