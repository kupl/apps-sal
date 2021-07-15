pp = input()
if len(pp) == 1:
    print('0')
    return
z = 1 if pp[0]=='0' else 0
zc = [z]
l = 1
lndl = [l]
for p in pp[1:]:
    l = max(z + 1, l + (1 if p == '1' else 0))
    z += 1 if p == '0' else 0
    lndl.append(l)
    zc.append(z)
lnda = lndl[-1]
o = 1 if pp[-1]=='1' else 0
oc = [o]
l = 1
lndr = [l]
for p in reversed(pp[:-1]):
    l = max(o + 1, l + (1 if p == '0' else 0))
    o += 1 if p == '1' else 0
    lndr.append(l)
    oc.append(o)
oc.reverse()
lndr.reverse()
qq = []
ez = 0
if pp[0] == '1':
    if max(oc[1], lndr[1] + 1) != lnda :
        qq.append('1')
    else:
        qq.append('0')
        ez += 1
else:
    qq.append('0')
for p, l, o, z, r in zip(pp[1:-1],lndl, oc[2:], zc, lndr[2:]):
    if p == '1':
        if max(l + o, z + ez + 1 + r) != lnda:
            qq.append('1')
        else:
            qq.append('0')
            ez += 1
    else:
        qq.append('0')

qq.append('0')
print(''.join(qq))

