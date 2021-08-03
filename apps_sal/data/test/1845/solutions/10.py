
n = int(input())
arr = list(map(int, input().strip().split()))

x = sum(arr)
arr = sorted(arr)
ans = [x]
for i in range(n - 1, -1, -1):
    for j in range(1, arr[i] + 1):
        if arr[i] % j == 0:
            if arr[i] + arr[0] > (arr[i] // j) + arr[0] * j:
                ans.append(x - arr[i] - arr[0] + arr[0] * j + (arr[i] // j))

print(min(ans))
