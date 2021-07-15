s = input()
n = len(s)

#iよりleftのA、rightのC, leftの？, rightの?
la = [0 for _ in range(n)]
rc = [0 for _ in range(n)]
lq = [0 for _ in range(n)]
rq = [0 for _ in range(n)]

for i in range(n-1):
    if s[i] == 'A':
        la[i+1] = 1
    if s[i] == '?':
        lq[i+1] = 1
    if s[i+1] == '?':
        rq[i] = 1
    if s[i+1] == 'C':
        rc[i] = 1

for i in range(n-1):
    la[i+1] += la[i]
    lq[i+1] += lq[i]

for i in range(n-1, 0, -1):
    rc[i-1] += rc[i]
    rq[i-1] += rq[i]

ans = 0
mod = 10 ** 9 + 7

for i in range(n):
    if s[i] in ['B', '?']:
        l = la[i] * pow(3, lq[i], mod)
        if lq[i] > 0:
            l += lq[i] * pow(3, lq[i]-1, mod)
            l %= mod

        r = rc[i] * pow(3, rq[i], mod)
        if rq[i] > 0:
            r += rq[i] * pow(3, rq[i]-1, mod)
            r %= mod
        ans += l * r
        ans %= mod


print(ans)
