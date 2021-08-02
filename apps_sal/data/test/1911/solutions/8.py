n, k = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
k -= 1
arr_new = sorted([arr[i + 1] - arr[i] for i in range(n - 1)], reverse=True)
print(arr[-1] - arr[0] - sum(arr_new[:k]))
