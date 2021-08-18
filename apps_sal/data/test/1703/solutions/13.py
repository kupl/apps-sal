n = int(input().strip())
c1 = 0
f = {}
s = {}
for i in range(n):
    c = 0
    minm = 1000000
    st = input().strip()
    for j in st:
        if j == '(':
            c += 1
        else:
            c -= 1
        minm = min(minm, c)
    if(c == 0 and minm >= 0):
        c1 += 1
    elif c < 0 and minm == c:
        if c in s:
            s[c] += 1
        else:
            s[c] = 1
    elif c > 0 and minm >= 0:
        if c in f:
            f[c] += 1
        else:
            f[c] = 1
c2 = 0
for i in f.keys():
    if (-1 * i) in s:
        c2 += f[i] * s[(-1 * i)]
print((c1 * c1) + c2)
