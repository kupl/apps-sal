import math
n = int(input())

a = []
t = []
s = 0
for _ in range(n):

    f = float(input())
    p = 0
    if f.is_integer():
        t.append(0)
        p = int(f)
    else:
        p = int(math.floor(f))
        t.append(-1)
    a.append(p)
    s += p

for i, e in enumerate(a):
    if t[i] == 0:
        print(e)
    elif s == 0:
        print(e)
    else:
        print(e + 1)
        s += 1
