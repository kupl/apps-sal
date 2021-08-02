n = int(input())
arr = list(map(int, input().split()))
res = float('inf')
for i in range(1, n):
    res = min(res, min(arr[i], arr[0]) // i)
for i in range(n - 1):
    res = min(res, min(arr[i], arr[n - 1]) // (n - 1 - i))
print(res)
