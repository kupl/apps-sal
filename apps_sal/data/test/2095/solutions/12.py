n = int(input())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))
ans = [0] * n
for i in range(n):
    for j in range(n):
        if ar[i][j] == 1 or ar[i][j] == 3:
            ans[i] = 1
        if ar[i][j] == 2:
            ans[j] = 1
ans1 = []
for i in range(n):
    if ans[i] == 0:
        ans1.append(i + 1)
print(len(ans1))
for i in range(len(ans1)):
    print(ans1[i], end=' ')
