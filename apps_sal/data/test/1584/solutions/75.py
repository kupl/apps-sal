from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for small in range(n - 2):
    for mid in range(small + 1, n - 1):
        div = bisect_left(arr, arr[small] + arr[mid], 0, n)
        if div > mid + 1:
            ans += div - mid - 1
print(ans)
