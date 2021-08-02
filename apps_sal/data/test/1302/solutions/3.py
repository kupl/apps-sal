n, k = map(int, input().split())
a = [i + 1 for i in range(n)]
if n == k:
    print(-1)
else:
    for i in range(n - k - 1):
        a[0], a[n - 1 - i] = a[n - i - 1], a[0]
    print(*a)
