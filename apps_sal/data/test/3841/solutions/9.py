(p, k) = list(map(int, input().split()))
coeff = [1]
maxi = k - 1
kk = k * k
while maxi < p:
    for i in range(2):
        coeff.append(0)
    maxi += kk * (k - 1)
    kk *= k * 2
n = len(coeff)
powk = [0 for i in range(n)]
pos = [0 for i in range(n)]
neg = [0 for i in range(n)]
powk[0] = 1
for i in range(1, n):
    powk[i] = powk[i - 1] * k
pos[0] = k - 1
neg[0] = 0
for i in range(1, n):
    if i % 2 == 0:
        pos[i] = pos[i - 1] + powk[i] * (k - 1)
        neg[i] = neg[i - 1]
    else:
        pos[i] = pos[i - 1]
        neg[i] = neg[i - 1] + powk[i] * (k - 1)
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        coeff[i] = (p + neg[i]) // powk[i]
        p -= coeff[i] * powk[i]
    else:
        coeff[i] = (-p + pos[i]) // powk[i]
        p += coeff[i] * powk[i]
ng = False
for i in range(n):
    if coeff[i] >= k:
        ng = True
if ng:
    print(-1)
else:
    d = n
    for i in range(n - 1, -1, -1):
        if coeff[i] == 0:
            d = d - 1
        else:
            break
    print(d)
    print(' '.join(map(str, coeff[0:d])))
