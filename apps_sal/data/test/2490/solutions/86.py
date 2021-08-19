s = input()
n = len(s)
s = list(map(int, list(s)))
dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)
dp2[0] = 1
for k in range(n):
    dp1[k + 1] = min([dp1[k] + s[k], dp2[k] + 10 - s[k]])
    dp2[k + 1] = min([dp1[k] + s[k] + 1, dp2[k] + 10 - s[k] - 1])
print(dp1[-1])
