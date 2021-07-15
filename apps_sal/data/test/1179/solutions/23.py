n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = n - 1
for i in range(1, n + 1):
    if (1 + i) * i // 2 >= k:
        ans = i - 1
        break
print(arr[k - (1 + ans) * ans // 2 - 1])

