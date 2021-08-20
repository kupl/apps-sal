(n, m) = list(map(int, input().split()))
a = [0] * 100001
a[0] = 1
a[1] = 1
p = 1000000007
for i in range(2, 100001):
    a[i] = (a[i - 1] + a[i - 2]) % p
print((a[n] + a[m] - 1) * 2 % p)
