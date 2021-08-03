n, T = list(map(int, input().split(' ')))
r = list()
r.append(list(map(int, input().split(' '))))
r.append(list(map(int, input().split(' '))))
r.append(list())
for i in range(len(r[0])):
    r[2].append((r[0][i], r[1][i]))
r[2].sort(key=lambda x: x[::-1])
for i in range(n):
    r[0][i] = r[2][i][0]
    r[1][i] = r[2][i][1]

fl = True
tau = sum(r[0]) * T > sum(map(lambda x: x[0] * x[1], r[2]))
if tau:
    r[2].reverse()
    fl = False
tau1 = not tau

summ = list()
proi = list()
su = 0
pr = 0
for i in range(n):
    su += r[2][i][0]
    summ.append(su)
    pr += r[2][i][0] * r[2][i][1]
    proi.append(pr)

lev = 0
pra = n - 1
while lev < n - 1 and ((r[2][lev][1] <= T and fl) or
                       (r[2][lev][1] >= T and not fl)):
    lev += 1
test = lev

while lev != pra:
    tau = tau1
    tau1 = summ[(lev + pra) // 2 - 1] * T > proi[(lev + pra) // 2 - 1]
    if tau == tau1:
        lev = (lev + pra) // 2 + 1
    else:
        pra = (lev + pra) // 2
        tau1 = not tau1

tau = summ[-1] * T > proi[-1]
tau1 = summ[max(pra - 1, 0)] * T > proi[max(pra - 1, 0)]
if tau != tau1:
    x = ((summ[max(pra - 1, 0)] * T) - proi[max(pra - 1, 0)]) / (
        r[2][pra][1] - T)
    x = summ[max(pra - 1, 0)] + x
    print(x)
else:
    tau = tau1
    tau1 = summ[max(lev - 2, 0)] * T > proi[max(lev - 2, 0)]
    if tau != tau1:
        x = ((summ[max(lev - 2, 0)] * T) - proi[max(lev - 2, 0)]) / (
            r[2][max(lev - 1, 0)][1] - T)
        x = summ[max(lev - 2, 0)] + x
        print(x)
    else:
        x = 0
        if test == 0 or test == 1:
            if r[2][0][1] == T:
                x = r[2][0][0]
        else:
            if r[2][test][1] != T:
                test -= 1
            x = summ[test]
            while test > -1 and r[2][test][1] == T:
                test -= 1
            if test != -1:
                x -= summ[test]
        print(x)
