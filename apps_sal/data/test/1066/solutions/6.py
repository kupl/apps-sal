n, k = list(map(int, input().split()))
m = n // 2 + n % 2
if k <= m:
    print(2 * k - 1)
else:
    print(2 * (k - m))
