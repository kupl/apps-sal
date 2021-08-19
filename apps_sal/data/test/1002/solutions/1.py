(n, d) = map(int, input().split())
t = list(map(int, input().split()))
T = sum(t) + 10 * (n - 1)
if T > d:
    print(-1)
else:
    print(2 * (n - 1) + (d - T) // 5)
