N = int(input())
arr = list(map(str, input()))

ans = 1
for i in range(N - 1):
    if arr[i] != arr[i + 1]:
        ans += 1

print(ans)
