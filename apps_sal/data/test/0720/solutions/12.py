
n = int(input())

arr = []

for i in range(n):
    a, b = list(map(int, input().strip().split()))
    arr.append([a, b])

ans = 1
la = [0, 0]

for i in range(n):
    if i == 0:
        ans += min(arr[i][0], arr[i][1])
    else:
        if arr[i - 1][0] == arr[i - 1][1]:
            c = 0
        else:
            c = 1
        ans += max(0, c + min(arr[i][0], arr[i][1]) - max(arr[i - 1][0], arr[i - 1][1]))
print(ans)
