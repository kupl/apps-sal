from collections import Counter


def isSubseq(s, x):
    (i, j) = (0, 0)
    while True:
        if j == len(x):
            return True
        if i == len(s):
            return False
        if s[i] == x[j]:
            j += 1
        i += 1


for _ in range(int(input().strip())):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    if not isSubseq(t, s):
        print('NO')
        continue
    (cs, ct, cp) = (Counter(s), Counter(t), Counter(p))
    newc = {}
    for key in cs:
        newc[key] = cs[key]
    for key in cp:
        if key in list(newc.keys()):
            newc[key] += cp[key]
        else:
            newc[key] = cp[key]
    wrong = False
    for key in ct:
        if key in list(newc.keys()):
            if newc[key] < ct[key]:
                wrong = True
                break
        else:
            wrong = True
            break
    if wrong:
        print('NO')
    else:
        print('YES')
