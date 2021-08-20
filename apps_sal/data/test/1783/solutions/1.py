(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
movSum = sum(a[0:k])
tot = movSum
for i in range(1, n - k + 1):
    movSum -= a[i - 1]
    movSum += a[i + k - 1]
    tot += movSum
print(tot / (n - k + 1))
