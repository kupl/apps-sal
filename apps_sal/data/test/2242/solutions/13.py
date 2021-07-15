s = input()
t = s[::-1]
n = len(s)
resid = [0] * 2019
resid[0] = 1
csum = 0
powoften = 1
for i in range(n):
    csum = (csum + int(t[i]) * powoften) % 2019
    powoften = (10 * powoften) % 2019
    resid[csum] += 1
ans = 0
for i in range(2019):
    ans += resid[i] * (resid[i] - 1) // 2
print(ans)
