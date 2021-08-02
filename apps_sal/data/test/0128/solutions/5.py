n, k = list(map(int, input().split()))
if (k > n // 2):
    k = n // 2
if n == 1 or k == 0:
    print(0)
else:
    print(k * (2 * n - 2 * k - 1))
