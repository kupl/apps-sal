t = int(input())
for _ in range(t):
    (n, m, a, b) = map(int, input().split())
    print(max(max(a, n - a - 1) * m, max(b, m - b - 1) * n))
