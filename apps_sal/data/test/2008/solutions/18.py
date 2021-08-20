n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1] - x[0])
res = 0
for i in range(n):
    res += arr[i][0] * i + arr[i][1] * (n - i - 1)
print(res)
