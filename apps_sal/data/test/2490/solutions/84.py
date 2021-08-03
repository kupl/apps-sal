N = input()

dp0 = [0] * (len(N) + 1)
dp1 = [0] * (len(N) + 1)
dp1[0] = 1

for i in range(len(N)):
    n = int(N[i])
    dp0[i + 1] = min(dp0[i] + n, dp1[i] + (10 - n))
    n += 1
    dp1[i + 1] = min(dp0[i] + n, dp1[i] + (10 - n))

# print(dp0)
# print(dp1)
print((dp0[-1]))
