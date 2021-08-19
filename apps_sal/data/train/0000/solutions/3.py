t = int(input())
for _ in range(t):
    n = int(input())
    k = {'01': 0, '00': 0, '11': 0, '10': 0}
    ab = []
    ba = []
    a = []
    ra = set()
    rb = set()
    for i in range(n):
        s = input()
        ts = s[0] + s[-1]
        k[ts] += 1
        if ts == '01':
            ab.append([str(i + 1), s])
            ra.add(s)
        if ts == '10':
            ba.append([str(i + 1), s])
            rb.add(s)
    if k['01'] == 0 and k['10'] == 0 and (k['00'] > 0) and (k['11'] > 0):
        ans = -1
    elif k['01'] == k['10'] or k['01'] == k['10'] + 1 or k['01'] == k['10'] - 1:
        ans = 0
    else:
        m = (k['01'] + k['10']) // 2 if (k['01'] + k['10']) % 2 == 0 else (k['01'] + k['10']) // 2 + 1
        if k['01'] > m:
            ans = k['01'] - m
            for i in range(len(ab)):
                psp = ab[i][1]
                nn = list(psp)
                nn.reverse()
                psp = ''.join(nn)
                c1 = len(rb)
                rb.add(psp)
                c2 = len(rb)
                if c1 != c2:
                    a.append(ab[i][0])
            if len(a) >= ans:
                a = a[:ans]
            else:
                ans = -1
        else:
            ans = k['10'] - m
            for i in range(len(ba)):
                psp = ba[i][1]
                nn = list(psp)
                nn.reverse()
                psp = ''.join(nn)
                c1 = len(ra)
                ra.add(psp)
                c2 = len(ra)
                if c1 != c2:
                    a.append(ba[i][0])
            if len(a) >= ans:
                a = a[:ans]
            else:
                ans = -1
    print(ans)
    if ans > 0:
        print(' '.join(a))
