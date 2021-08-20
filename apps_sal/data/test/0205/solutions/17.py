from math import sqrt as S
(n, b) = map(int, input().split())
temp = b
pf = []
for i in range(2, int(S(b)) + 1):
    if b % i == 0:
        c = 0
        while b % i == 0:
            c += 1
            b = b // i
        pf.append([c, i])
if b > 1:
    pf.append([1, b])
plen = len(pf)


def chk(z, p):
    ct = 0
    k = p
    while z // k > 0:
        ct += z // k
        k = k * p
    return ct


mini = 10 ** 50
for i in range(plen):
    currp = pf[i][1]
    cnt = pf[i][0]
    cur = chk(n, currp)
    mini = min(mini, cur // cnt)
print(mini)
