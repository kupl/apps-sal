from itertools import combinations


def is_perfect_square(n):
    return round(n ** 0.5) ** 2 == n


s = input()
ls = len(s)
sl = [i for i in s]
x = []
for i in range(1, len(s) + 1):
    comb = combinations(sl, i)
    for j in list(comb):
        x.append(list(j))
y = []
for i in x:
    a = ''
    for j in i:
        a += j
    y.append(int(a))
y = list(set(y))
y.sort(reverse=True)
f = 0
for i in y:
    if i != 0:
        if is_perfect_square(i):
            f = 1
            break
if f:
    print(ls - len(str(i)))
else:
    print(-1)
