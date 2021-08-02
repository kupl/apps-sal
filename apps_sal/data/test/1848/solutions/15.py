n = int(input())
x = [int(z) for z in input().split()]
x.sort()
y = []
cur = x[0]
curs = 1
i = 1
y = []
while i < n:
    r = x[i]
    if r == cur:
        curs += 1
    else:
        d = [cur] * curs
        y += [d]
        curs = 1
        cur = r
    i += 1
y += [[cur] * curs]
res = 0

while len(y) > 1:
    u = []
    for h in y:
        h.pop()
        if h != []:
            u += [h]
    res += len(y) - 1
    y = u[:]
print(res)
