n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))
a = sorted(arr)
m = 10**9
for i in range(n - k + 1):
    ma = a[i + k - 1] - a[i]
    m = min(m, ma)
print(m)
