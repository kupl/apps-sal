(n, k) = [int(i) for i in input().split()]
if k % 2 == 1:
    print((n // k) ** 3)
else:
    print((n // k) ** 3 + (n // k + n % k // (k // 2)) ** 3)
