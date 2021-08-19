(n, m) = [int(x) for x in input().split()]
a = [[0] * m for i in range(n)]
for i in range(n):
    a[i] = list(input())
i = 0
j = 0
ans1 = 0
ans2 = 0
cnt = 0
temp = [0] * m
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            temp[j] += 1
for i in range(1, m):
    ans1 = max(ans1, temp[i] - temp[i - 1])
    ans2 = max(ans2, temp[i - 1] - temp[i])
print(ans1, ans2)
