n, k = list(map(int, input().split()))
res = 0
if k == 0:
    print((n * n))
else:
    for i in range(k + 1, n + 1):
        res += (n // i) * (i - k) + max(0, n % i - k + 1)
    print(res)

