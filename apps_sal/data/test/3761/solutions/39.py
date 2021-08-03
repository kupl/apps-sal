s = input()
x, y = map(int, input().split())
cnt = 0
xm = []
ym = []
flag = True

for i in range(len(s)):
    if s[i] == 'F':
        cnt += 1
    else:
        if flag:
            xm.append(cnt)
            flag = False
        else:
            ym.append(cnt)
            flag = True

        cnt = 0

if flag:
    xm.append(cnt)
else:
    ym.append(cnt)

s = {0}

for i in range(len(xm)):
    ns = set()

    if i == 0:
        for si in s:
            ns.add(si + xm[i])
    else:
        for si in s:
            ns.add(si - xm[i])
            ns.add(si + xm[i])

    s = ns

if x not in ns:
    print('No')
    return

s = {0}

for i in range(len(ym)):
    ns = set()

    for si in s:
        ns.add(si - ym[i])
        ns.add(si + ym[i])

    s = ns

if y not in s:
    print('No')
    return

print('Yes')
