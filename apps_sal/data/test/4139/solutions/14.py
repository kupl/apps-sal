from itertools import product
n = int(input())


def gen357():
    for i in range(3, 11):
        for s in product('357', repeat=i):
            tmp = ''.join(s)
            if '3' in tmp and '5' in tmp and ('7' in tmp):
                yield int(''.join(s))


for (i, ans) in enumerate(gen357(), 1):
    if ans > n:
        print(i - 1)
        break
