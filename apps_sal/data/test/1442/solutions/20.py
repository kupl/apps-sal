s = input()
(n, d) = (int(s.split()[0]), int(s.split()[1]))
(b, s) = ({}, {})
(wb, ws) = ([], [])
for i in range(0, n):
    st = input().split()
    st[1] = int(st[1])
    st[2] = int(st[2])
    if st[0] == 'B':
        if st[1] not in b:
            b[st[1]] = st[2]
        else:
            b[st[1]] += st[2]
        if st[1] not in wb:
            wb.append(st[1])
    else:
        if st[1] not in s:
            s[st[1]] = st[2]
        else:
            s[st[1]] += st[2]
        if st[1] not in ws:
            ws.append(st[1])
ws.sort()
wb.sort(reverse=True)
ws = ws[:d]
wb = wb[:d]
ws.sort(reverse=True)
for i in ws:
    print('S %s %s' % (i, s[i]))
for i in wb:
    print('B %s %s' % (i, b[i]))
