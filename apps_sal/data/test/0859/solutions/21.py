from math import factorial


def C(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))


str1 = input()
str2 = input()
pos1 = 0
pos2 = 0
need = 0
for i in str1:
    if i == '+':
        pos1 += 1
    else:
        pos1 -= 1

for i in str2:
    if i == '+':
        pos2 += 1
    elif i == '-':
        pos2 -= 1
    else:
        need += 1

diff = abs(pos1 - pos2)
if diff % 2 != need % 2:
    print(0)
else:
    if need == 0:
        if pos1 == pos2:
            print(1)
        else:
            print(0)

    elif diff > need:
        print(0)
    else:
        a = (need + diff) // 2
        print(C(need, a) / (2**need))
