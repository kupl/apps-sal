n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]
ans = 0
for i in range(n):
    ans = max(ans, sum(arr[0][:i + 1] + arr[1][i:]))
else:
    print(ans)
