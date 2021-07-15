n, L = list(map(int, input().split()))
pr = list(map(int, input().split()))
res = 0
poss = []
ber = [(pr[i] / 2 ** i, i) for i in range(n)]
ber.sort()
for i in range(n):
    d = L // (2 ** ber[i][1])
    res += d * pr[ber[i][1]]
    L -= d * (2 ** ber[i][1])
    if L == 0:
        poss.append(res)
    poss.append(res + pr[ber[i][1]])
print(min(poss))

