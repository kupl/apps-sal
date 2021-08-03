k, n = map(int, input().split())
a = list(map(int, input().split()))
temp = 0
for i in range(n - 1):
    temp = max(temp, a[i + 1] - a[i])
temp = max(temp, k - a[n - 1] + a[0])
print(k - temp)
