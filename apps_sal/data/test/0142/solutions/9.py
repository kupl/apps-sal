n, l = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    arr[i] = min(arr[i], arr[i - 1] * 2)
for i in range(64):
    arr.append(arr[-1] * 2)
dp = 0
for i in range(64):
    if ((l >> i) & 1):
        dp += arr[i]
    else:
        dp = min(dp, arr[i])
print(dp)
