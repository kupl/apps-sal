s = input()
p = input()
t1 = int(s[len(s) - 2:len(s)]) - int(p[len(p) - 2:len(p)])
k = 0
if t1 < 0:
    t1 += 60
    k = 1
t0 = int(s[:2]) - int(p[:2]) - k
while t0 < 0:
    t0 += 24
t0 %= 24
res = str(t0) + ':'
if len(res) < 3:
    res = '0' + res
ss = '0' + str(t1)
ss = ss[-2:]
res += ss
print(res)
