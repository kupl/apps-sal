n = int(input())
s = []
ans = []
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(n):
    f = True
    for j in range(n):
        if s[i][j] == 1 or s[j][i] == 2 or s[i][j] == 3 or s[j][i] == 3:
            f = False
    if f:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i + 1, end=' ')
