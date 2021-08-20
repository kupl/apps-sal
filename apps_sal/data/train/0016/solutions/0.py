from math import sqrt


class pro(object):

    def __init__(self, dif, sc):
        self.dif = dif
        self.sc = sc

    def __lt__(self, other):
        return self.dif > other.dif


T = int(input())
mul = [1]
for i in range(100):
    mul.append(mul[i] * 10 / 9)
inf = 1000000007
for t in range(T):
    n = int(input())
    (effi, tim) = list(map(float, input().split()))
    prob = []
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        prob.append(pro(x, y))
    prob.sort()
    f = [[inf for i in range(n + 1)] for j in range(1001)]
    f[0][0] = 0
    totsc = 0
    for i in range(n):
        totsc += prob[i].sc
        for j in range(totsc, prob[i].sc - 1, -1):
            for k in range(1, i + 2):
                f[j][k] = min(f[j][k], f[j - prob[i].sc][k - 1] + prob[i].dif * mul[k])
    for i in range(totsc, -1, -1):
        flag = False
        for j in range(n + 1):
            if sqrt(effi * f[i][j]) >= 1:
                res = 2 * sqrt(f[i][j] / effi) - 1 / effi + 10 * j
            else:
                res = f[i][j] + 10 * j
            if res <= tim:
                print(i)
                flag = True
                break
        if flag == True:
            break
