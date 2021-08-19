# we love abc
s = input()
mod = 10**9 + 7
dpa = [[0, 0] for i in range(len(s) + 1)]
dpc = [[0, 0] for i in range(len(s) + 1)]
power3 = [1 for i in range(10**5 + 100)]
for i in range(10**5 + 3):
    power3[i + 1] = (power3[i] * 3) % mod
for i in range(len(s)):
    if s[i] == "A":
        dpa[i + 1][0] = (dpa[i][0] + power3[dpa[i][1]]) % mod
        dpa[i + 1][1] = dpa[i][1]
    elif s[i] == "?":
        dpa[i + 1][0] = (3 * dpa[i][0] + power3[dpa[i][1]]) % mod
        dpa[i + 1][1] = dpa[i][1] + 1
    else:
        dpa[i + 1] = dpa[i]
for i in range(len(s)):
    if s[len(s) - 1 - i] == "C":
        dpc[i + 1][0] = (dpc[i][0] + power3[dpc[i][1]]) % mod
        dpc[i + 1][1] = dpc[i][1]
    elif s[len(s) - 1 - i] == "?":
        dpc[i + 1][0] = (3 * dpc[i][0] + power3[dpc[i][1]]) % mod
        dpc[i + 1][1] = dpc[i][1] + 1
    else:
        dpc[i + 1] = dpc[i]
ans = 0
for i in range(1, len(s) - 1):
    if s[i] == "B" or s[i] == "?":
        ans += dpa[i][0] * dpc[len(s) - 1 - i][0]
        ans = ans % mod
print(ans)
