def prov(la, lb, lc, ld):
    if la/lb >= 2 and la/lc >= 2 and la/ld >= 2:
        return True
    return False
def prov1(la, lb, lc, ld):
    if  lb/la >= 2 and lc/la >= 2 and ld/la >= 2:
        return True
    return False
a = list(input())
b = list(input())
c = list(input())
d = list(input())
a = a[2:]
b = b[2:]
c = c[2:]
d = d[2:]
la = len(a)
lb = len(b)
lc = len(c)
ld = len(d)
q = []
if prov(la, lb, lc, ld) or prov1(la, lb, lc, ld):
    q.append('A')
if prov(lb, la, lc, ld) or prov1(lb, la, lc, ld):
    q.append('B')
if prov(lc, la, lb, ld) or prov1(lc, ld, la, lb):
    q.append('C')
if prov(ld, la, lb, lc) or prov1(ld, la, lb, lc):
    q.append('D')
if len(q) == 1:
    print(q[0])
else:
    print('C')
