__author__ = 'Utena'


def t(x):
    c = 0
    if x % 5 == 0:
        return t(x // 5) + 1
    else:
        return 0


m = int(input())
i = 5
n = 0
c = []
t1 = 0
while True:
    n += t(i)
    if n == m:
        t1 += 1
        c.append(str(i))
    if n > m:
        break
    i += 1
if t1 == 0:
    print(0)
else:
    print(t1)
    print(' '.join(c))
