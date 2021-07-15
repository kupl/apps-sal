alp = set(input())
pt = input()
lp= pt.split('*')[0]
rp = ''
if len(pt.split('*')) > 1:
    rp = pt.split('*')[1]
n = int(input())

def check(p, qp):
    for i in range(len(p)):
        if p[i] == qp[i] or (p[i] == '?' and qp[i] in alp):
            continue
        else:
            return False
    return True

def checks(qp):
    for i in range(len(qp)):
        if qp[i] not in alp:
            continue
        else: 
            return False
    return True

for i in range(n):
    q = input()
    if len(lp) + len(rp) > len(q) or ('*' not in pt and len(lp) < len(q)):
        print('NO')
        continue
    qlp = q[:len(lp)]
    qrp = q[(len(q) - len(rp)):]
    star = q[len(lp):(len(q) - len(rp))]
    if check(lp, qlp) and check(rp, qrp) and checks(star):
        print('YES')
    else:
        print('NO')
