import math
from decimal import Decimal, ROUND_HALF_UP


def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // math.gcd(x, a[i])
    return x


def gcd(a):
    temp = math.gcd(a[0], a[1])
    for i in a:
        temp = math.gcd(temp, i)
    return temp


n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
zero = False
count = 0
#a = list(map(lambda x: x // 2, na))
mini = lcm(a)
if len(a) != 1:
    maxi = gcd(a)
else:
    maxi = a[0]
maxi2 = maxi
nibai = 1
while(True):
    if maxi2 % 2 == 0:
        nibai *= 2
        maxi2 //= 2
    else:
        break
for i in a:
    if i % (2 * nibai) == 0:
        zero = True
        break
#print(nibai, maxi, mini)
if not zero:
    t = Decimal(str((m * 2 // mini) / 2))
    # print(t)
    print(t.quantize(Decimal('0'), rounding=ROUND_HALF_UP))
else:
    print(0)
