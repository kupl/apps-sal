n, k = list(map(int, input().split()))

a = 0 if k == 0 or k == n else 1
b = min(2 * k, n - k)
print("%d %d" % (a, b))

