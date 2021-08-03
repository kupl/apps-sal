t = int(input())
for _ in range(t):
    n, x, a, b = map(int, input().split())

    ans = min(n - 1, abs(a - b) + x)
    print(ans)
