a, b, c, n = list(map(int, input().split()))
if c <= min(a, b) and max(a, b) < n and n - a - b + c >= 1:
    print(n - a - b + c)
else:
    print(-1)
