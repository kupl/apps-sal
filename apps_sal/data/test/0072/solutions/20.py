n = int(input())
a = input()
b = input()
c = input()
Da = {}
Db = {}
Dc = {}
al = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in al:
    Da[i] = 0
    Db[i] = 0
    Dc[i] = 0
for j in a:
    Da[j] += 1
for j in b:
    Db[j] += 1
for j in c:
    Dc[j] += 1
pa = 0
ia = 0
pb = 0
ib = 0
pc = 0
ic = 0
for x in Da:
    if Da[x] % 2 == 0:
        pa = max(pa, Da[x])
    else:
        ia = max(ia, Da[x])
for x in Db:
    if Db[x] % 2 == 0:
        pb = max(pb, Db[x])
    else:
        ib = max(ib, Db[x])
for x in Dc:
    if Dc[x] % 2 == 0:
        pc = max(pc, Dc[x])
    else:
        ic = max(ic, Dc[x])
t = len(a)
a1 = 0
a2 = 0
if pa + n <= t:
    a1 = pa + n
else:
    a1 = t
if ia + n <= t:
    a2 = ia + n
else:
    a2 = t
b1 = 0
b2 = 0
if pb + n <= t:
    b1 = pb + n
else:
    b1 = t
if ib + n <= t:
    b2 = ib + n
else:
    b2 = t
c1 = 0
c2 = 0
if pc + n <= t:
    c1 = pc + n
else:
    c1 = t
if ic + n <= t:
    c2 = ic + n
else:
    c2 = t
A = max(a1, a2)
B = max(b1, b2)
C = max(c1, c2)
if (pa == t or ia == t) and n == 1:
    A = t - 1
if (pb == t or ib == t) and n == 1:
    B = t - 1
if (pc == t or ic == t) and n == 1:
    C = t - 1
if A > B and A > C:
    print("Kuro")
elif B > A and B > C:
    print("Shiro")
elif C > A and C > B:
    print("Katie")
else:
    print("Draw")
