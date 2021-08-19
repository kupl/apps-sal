(n, m, k) = map(int, input().split())
if n != m:
    print(min(n, m) * 2 + 1 + 2 * k)
else:
    print(n * 2 + 2 * k)
