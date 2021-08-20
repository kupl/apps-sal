n = int(input())
arr = list(map(int, input().strip().split(' ')))
ans = []
cnt = 0
temp = []
temp.append(1)
for i in range(1, n):
    if arr[i] == 1:
        ans.append(temp)
        temp = [1]
    else:
        temp.append(arr[i])
if len(temp) != 0:
    ans.append(temp)
print(len(ans))
for i in ans:
    print(i[len(i) - 1], end=' ')
