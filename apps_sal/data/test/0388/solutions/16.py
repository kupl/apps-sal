(n, k) = [int(i) for i in input().split()]
s = [i for i in input().split()]
res = []
c1 = ord('A')
c2 = ord('a')
c3 = ord('a')
for i in range(0, k - 1):
    res1 = ''
    if c1 == ord('Z') and c2 == ord('z'):
        res1 = chr(c1) + chr(c2) + chr(c3)
        c3 += 1
    elif c1 == ord('Z'):
        res1 = chr(c1) + chr(c2)
        c2 += 1
    else:
        res1 = chr(c1)
        c1 += 1
    res.append(res1)
for i in range(len(s)):
    if s[i] == 'NO':
        res.append(res[i])
    else:
        res1 = ''
        if c1 == ord('Z') and c2 == ord('z'):
            res1 = chr(c1) + chr(c2) + chr(c3)
            c3 += 1
        elif c1 == ord('Z'):
            res1 = chr(c1) + chr(c2)
            c2 += 1
        else:
            res1 = chr(c1)
            c1 += 1
        res.append(res1)
for i in res:
    print(i, end=' ')
