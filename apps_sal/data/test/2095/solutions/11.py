n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if A[i][j] == 1 or A[i][j] == 3:
            break
    else:
        cnt += 1
        ans.append(i + 1)
print(cnt)
for i in ans:
    print(i, end=' ')
