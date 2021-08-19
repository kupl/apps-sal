def isNumber(x):
    try:
        p = int(x)
        return x == str(p)
    except:
        return False


def conc(p):
    if len(p) == 0:
        return '-'
    s = '"'
    for i in range(len(p) - 1):
        s += p[i] + ','
    s += p[len(p) - 1] + '"'
    return s


s = input().split(';')
p = []
q = []
for l in s:
    for i in l.split(','):
        if isNumber(i):
            p.append(i)
        else:
            q.append(i)
p = conc(p)
q = conc(q)
print(p)
print(q)
