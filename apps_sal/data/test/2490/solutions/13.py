N = input()
dp0 = 0
dp1 = 1
for n in N:
    n = int(n)
    dp0_new = min(dp0 + n, dp1 + (10 - n))
    n = n + 1
    dp1_new = min(dp0 + n, dp1 + (10 - n))
    (dp0, dp1) = (dp0_new, dp1_new)
print(dp0)
