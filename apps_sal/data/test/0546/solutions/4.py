# IAWT
goods = input()

ptrn = input()
n = int(input())
qs = [input() for i in range(n)]

data = [False for i in range(26)]

for i in range(len(goods)):
    data[ord(goods[i]) - 97] = True

star_in = '*' in ptrn
if star_in:
    sind = ptrn.index('*')

theL = len(ptrn)


def f(q):
    if not star_in:
        if len(q) != theL:
            return False
        for i in range(theL):
            if ptrn[i] != '?':  # So should be exactly equal
                if ptrn[i] != q[i]:
                    return False
            elif not data[ord(q[i]) - 97]:
                return False
        return True
    if len(q) < theL - 1:
        return False
    for i in range(sind):
        if ptrn[i] == '?':
            if(not data[ord(q[i]) - 97]):
                return False
        elif ptrn[i] != q[i]:
            return False
    j = len(q) - 1
    for i in range(theL - 1, sind, -1):
        if ptrn[i] == '?':
            if (not data[ord(q[j]) - 97]):
                return False
        elif ptrn[i] != q[j]:
            return False
        j -= 1
    for i in range(sind, j + 1):
        if data[ord(q[i]) - 97]:
            return False
    return True


for i in range(n):
    if f(qs[i]):
        print('YES')
    else:
        print('NO')
