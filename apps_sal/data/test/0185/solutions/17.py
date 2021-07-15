n, k = map(int, input().split())
if 2 * k <= (n + 1):
    print(3 * n + k - 1)
else:
    print(4 * n - k)
