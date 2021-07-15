n, k = list(map(int, input().split()))

a = [0] * (n+1)
for i in range(1,n+1):
    a[i] = i

m = min(k, n >> 1)
for i in range(1,m+1):
    a[i], a[n-i+1] = a[n-i+1], a[i]

A = (n * (n - 1)) >> 1
l = n - m - m
l = (l * (l - 1)) >> 1
print(A - l)

