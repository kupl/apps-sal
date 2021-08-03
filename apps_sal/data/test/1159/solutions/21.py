

nre = int(input())


dpdfdjf = []


for i in range(nre - 1):

    dpdfdjf.append([i + 1, i + 2])


dpdfdjf.append([nre, 1])


kre = nre


def plotttt(xre):

    i = 2

    while (i ** 2 <= xre):

        if (xre % i == 0):

            return False

        i += 1

    return True


plotttts = [0] * 50000


for i in range(50000):

    plotttts[i] = (1 if plotttt(i) else 0)


wre = (nre + 2) // 2


mre = 1


while (wre <= nre):

    if (plotttts[kre] == 1):

        break

    else:

        dpdfdjf.append([mre, wre])

        mre += 1

        wre += 1

        kre += 1


print(len(dpdfdjf))


for i in range(len(dpdfdjf)):

    print(dpdfdjf[i][0], dpdfdjf[i][1])
