n = int(input())
(lsum, rsum) = (0, 0)
for i in range(n):
    (x, y) = map(int, input().split())
    lsum += x
    rsum += y
print(min(lsum, n - lsum) + min(rsum, n - rsum))
