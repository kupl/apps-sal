t = int(input())
for case in range(t):
    (n, x, a, b) = list(map(int, input().split()))
    dist = abs(b - a)
    ans = min(x + dist, n - 1)
    print(ans)
