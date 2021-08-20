s = input()
n = len(s)
ans = 0
dp1 = [0] * (n + 1)
dp0 = [0] * (n + 1)
dp1[0] = 1
for i in range(n):
    k = int(s[i])
    if k < 5:
        dp0[i + 1] = dp0[i] + k
    elif k > 5:
        dp0[i + 1] = dp1[i] + 10 - k
    elif i == 0:
        dp0[i + 1] = dp0[i] + k
    elif int(s[i - 1]) < 5:
        dp0[i + 1] = dp0[i] + k
    else:
        dp0[i + 1] = dp1[i] + 10 - k
    k += 1
    if k == 10:
        dp1[i + 1] = dp1[i]
    elif k < 5:
        dp1[i + 1] = dp0[i] + k
    elif k > 5:
        dp1[i + 1] = dp1[i] + 10 - k
    elif i == 0:
        dp1[i + 1] = dp0[i] + k
    elif int(s[i - 1]) < 5:
        dp1[i + 1] = dp0[i] + k
    else:
        dp1[i + 1] = dp1[i] + 10 - k
print(dp0[n])
