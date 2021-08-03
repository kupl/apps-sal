a, b, c = list(map(int, input().split()))
m = int(input())
d = {'USB': [], 'PS/2': []}
for _ in range(m):
    v, t = input().split()
    d[t].append(int(v))

d['PS/2'].sort()
d['USB'].sort()

eq = cst = f1 = f2 = 0
nusb = len(d['USB'])
nps2 = len(d['PS/2'])
while a > 0 and f1 < nusb:
    a -= 1
    eq += 1
    cst += d['USB'][f1]
    f1 += 1
while b > 0 and f2 < nps2:
    b -= 1
    eq += 1
    cst += d['PS/2'][f2]
    f2 += 1
while c > 0 and (f1 < nusb or f2 < nps2):
    c -= 1
    eq += 1
    if f1 == nusb:
        cst += d['PS/2'][f2]
        f2 += 1
        continue
    elif f2 == nps2:
        cst += d['USB'][f1]
        f1 += 1
        continue

    if d['PS/2'][f2] < d['USB'][f1]:
        cst += d['PS/2'][f2]
        f2 += 1
    else:
        cst += d['USB'][f1]
        f1 += 1

print(eq, cst)
