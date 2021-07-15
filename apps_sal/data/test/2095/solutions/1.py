n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))
    ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 or arr[i][j]== 3:
            break
    else:
        ans.append(i + 1)
print(len(ans))
if len(ans) != 0:
    print(*ans)
