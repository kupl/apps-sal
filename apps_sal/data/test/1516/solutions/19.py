

are = int(input())


dfhdsf = list(map(int, input().split()))


bre = []


zzre = len(str(dfhdsf[0]))


dfkhdjghdfd = [10**i for i in range(20)]


rre = 998244353


for i in dfhdsf:

    i = str(i)

    pre = 0

    qre = 0

    zre = 2 * zzre - 1

    z1re = 2 * zzre - 2

    for j in i:

        j = int(j)

        pre += j * dfkhdjghdfd[zre]

        qre += j * dfkhdjghdfd[z1re]

        zre -= 2

        z1re -= 2

    bre.append((((pre + qre) % rre) * (are)) % rre)


result = 0


for i in bre:

    result += i % rre


print(result % rre)
