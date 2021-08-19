(H, W) = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(10)]
wall = [list(map(int, input().split())) for i in range(H)]
for i in range(10):
    for j in range(10):
        for k in range(10):
            arr[j][k] = min(arr[j][i] + arr[i][k], arr[j][k])
ans = 0
for i in range(H):
    for item in wall[i]:
        if item < 0:
            continue
        ans += arr[item][1]
print(ans)
