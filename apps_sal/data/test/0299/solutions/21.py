def s(p):
    r = 0
    for i in range(len(p)):
        r += p[i]
    return r


n = int(input())
r = input()
l = list(r.split())
x = []
y = []
z = []
for i in range(len(l)):
    if i % 3 == 0:
        l[i] = int(l[i])
        y.append(l[i])
    elif i % 3 == 1:
        l[i] = int(l[i])
        z.append(l[i])
    else:
        l[i] = int(l[i])
        x.append(l[i])
if s(x) > s(y) and s(x) > s(z):
    print('back')
if s(y) > s(x) and s(y) > s(z):
    print('chest')
if s(z) > s(y) and s(z) > s(x):
    print('biceps')
