n, k = map(int, input().split())
a = list(map(int, input().split()))

result = 0

if a[0] > k:
    result = a[0] - k
    a[0] = k

for i in range(n - 1):
    if a[i] + a[i + 1] > k:
        result += a[i] + a[i + 1] - k
        a[i + 1] = -a[i] + k

print(result)
