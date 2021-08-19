# coding = utf-8
div = 1000000007
s = input()
n = len(s)
ans = 0

mi = [1]

for i in range(100):
    mi.append(mi[-1] * 2 % div)

for i in range(n):
    if s[n - 1 - i] == '1':
        ret = mi[i] * mi[i] % div * mi[n - 1 - i] % div
        ans = (ans + ret) % div
print(ans)
