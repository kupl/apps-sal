(n, m) = map(int, input().split())
sumx = 0
bigsum = (n - 1) * n // 2
mid = (n + 1) // 2
if n & 1:
    smallsum = mid * (mid - 1)
else:
    smallsum = mid * (mid - 1) + mid
for i in range(1, m + 1):
    (x, d) = map(int, input().split())
    sumx += x * n
    if d < 0:
        sumx += d * smallsum
    elif d > 0:
        sumx += d * bigsum
print('%.15f' % (sumx / n))
