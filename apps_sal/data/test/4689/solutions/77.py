k, n = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))

d_max = 0
a[0] = a[n] - k

for i in range(1, n + 1):
    d = a[i] - a[i - 1]
    d_max = max(d, d_max)

print((k - d_max))

