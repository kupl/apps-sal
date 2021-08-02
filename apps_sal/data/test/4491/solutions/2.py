N = int(input())
arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))

ans = 0
for i in range(0, N):
    x = sum(arr[0][:i + 1]) + sum(arr[1][i:])
    ans = max(ans, x)
print(ans)
