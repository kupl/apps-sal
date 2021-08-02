n, k = [int(i) for i in input().split()]
if k > n // 2 or n < 3 or n == 2 * k:
    print(-1)
    return
print(n * k)
arr = list(range(1, n + 1)) + list(range(1, n // 2 + 1))
for i in range(arr[arr.index(max(arr))]):
    for j in range(1, k + 1):
        print(arr[i], arr[j + i])
