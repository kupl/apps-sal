import sys
# sys.stdin = open('ivo.in')


def getkos(x, y):
    temp = (x[0] * y[0] + x[1] * y[1])
    mul = -1 if temp < 0 else 1
    return (mul * temp ** 2, (x[0] ** 2 + x[1] ** 2) * (y[0] ** 2 + y[1] ** 2))

class Drob:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __lt__(self, object):
        return self.num * object.denom < object.num * self.denom

n = int(sys.stdin.readline())

positive = []
negative = []
for i in range(n):
    x = tuple(map(int, sys.stdin.readline().split())) + (i,)
    if x[1] > 0:
        positive.append(x)
    else:
        negative.append(x)

positive.sort(key=lambda x: Drob((-1 if x[0] > 0 else 1) * x[0]**2 , (x[1] ** 2 +  x[0] ** 2)))
negative.sort(key=lambda x: Drob((1 if x[0] > 0 else -1) * x[0]**2 , (x[1] ** 2 +  x[0] ** 2)))
#negative.sort(key=lambda x,y: x[0] - y[0] if x[0] != y[0] else (y[1] - x[1]) * x[0])

all = positive + negative
# print(all)
biggest = [-1.1, 1]
bi = 0
bj = 1
for i in range(n):
    nxt = (i + 1) % n
    prev = (i + n - 1) % n

    kos1 = getkos(all[i], all[nxt])
    if kos1[1] * biggest[0] < kos1[0] * biggest[1]:
        biggest = kos1
        bi = all[i][2]
        bj = all[nxt][2]
    kos2 = getkos(all[i], all[prev])
    if kos2[1] * biggest[0] < kos2[0] * biggest[1]:
        biggest = kos2
        bi = all[i][2]
        bj = all[prev][2]
    # print("{} kos1: {} kos2: {}".format(i, kos1, kos2))

# print(biggest)
print("%d %d" % (bi + 1, bj+ 1))

