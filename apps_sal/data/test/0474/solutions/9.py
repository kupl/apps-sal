n = int(input())
arr = list(map(int, input().split()))
max1 = max(arr)
i = 0
ans = 1
while i < n:
    if arr[i] == max1:
        count = 0
        while i < n and arr[i] == max1:
            count += 1
            i += 1
        ans = max(ans, count)
    i += 1
print(ans)
