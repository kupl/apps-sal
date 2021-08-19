n = int(input())
name = [''] * n
surname = [''] * n
for i in range(n):
    (name[i], surname[i]) = input().split()
a = list(map(int, input().split()))
new_name = []
new_surname = []
for i in a:
    new_name.append(name[i - 1])
    new_surname.append(surname[i - 1])
dp = [[False] * 2 for i in range(n)]
dp[0][0] = True
dp[0][1] = True
for i in range(n - 1):
    if dp[i][0]:
        if new_name[i] < new_name[i + 1]:
            dp[i + 1][0] = True
        if new_name[i] < new_surname[i + 1]:
            dp[i + 1][1] = True
    if dp[i][1]:
        if new_surname[i] < new_name[i + 1]:
            dp[i + 1][0] = True
        if new_surname[i] < new_surname[i + 1]:
            dp[i + 1][1] = True
if dp[n - 1][0] or dp[n - 1][1]:
    print('YES')
else:
    print('NO')
