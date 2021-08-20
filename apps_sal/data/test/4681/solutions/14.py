n = int(input())
calc_r = [0] * (n + 1)
calc_r[0] = 2
calc_r[1] = 1
for i in range(2, n + 1):
    calc_r[i] = calc_r[i - 1] + calc_r[i - 2]
ans = calc_r[n]
print(ans)
