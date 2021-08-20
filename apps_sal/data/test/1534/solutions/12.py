str = input()
l = len(str)
cnt = 0
dp1 = 0
dp2 = 0
for i in range(l):
    if str[i] == 'a':
        cnt += 1
        dp2 = max(dp1 + 1, dp2 + 1)
    else:
        dp1 = max(dp1 + 1, cnt + 1)
print(max(dp1, dp2))
