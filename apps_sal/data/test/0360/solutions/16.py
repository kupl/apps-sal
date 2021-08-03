n = int(input())
arr = []
for i in range(n):
    a, b = list(map(int, input().split()))
    arr.append((a, b))
page = int(input())
ans = 0
for i in range(n):
    if(arr[i][0] <= page <= arr[i][1]):
        ans = i
print(n - ans)
