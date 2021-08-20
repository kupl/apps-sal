(n, x) = map(int, input().split())
arr = []
for _ in range(n):
    (l, r) = map(int, input().split())
    arr.append((l, r))
res = 0
res += (arr[0][0] - 1) % x
for i in range(n - 1):
    res += arr[i][1] - arr[i][0] + 1
    res += (arr[i + 1][0] - (arr[i][1] + 1)) % x
res += arr[n - 1][1] - arr[n - 1][0] + 1
print(res)
