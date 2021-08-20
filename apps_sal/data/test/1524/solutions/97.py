s = list(input())
lens = len(s)
lr = [[0] * 2 for i in range(lens)]
lrp = [0] * lens
icnt = 0
lr[0][0] = 1
for i in range(1, lens):
    if s[i] == 'R':
        if s[i - 1] == 'R':
            lr[icnt][0] += 1
        elif s[i - 1] == 'L':
            icnt += 1
            lr[icnt][0] += 1
    elif s[i] == 'L':
        if s[i - 1] == 'L':
            lr[icnt][1] += 1
        elif s[i - 1] == 'R':
            lr[icnt][1] += 1
            lrp[icnt] = i
ss = [0] * lens
for i in range(icnt + 1):
    r1 = lr[i][0] // 2
    r2 = lr[i][0] - r1
    l1 = lr[i][1] // 2
    l2 = lr[i][1] - l1
    ss[lrp[i]] = r1 + l2
    ss[lrp[i] - 1] = r2 + l1
tstr = str(ss[0])
for i in range(1, lens):
    tstr = tstr + ' ' + str(ss[i])
print(tstr)
