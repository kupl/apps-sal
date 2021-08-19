def m(good, pat, s):
    if len(pat) != len(s):
        return False
    else:
        for (u, v) in zip(pat, s):
            if u == '?':
                if v not in good:
                    return False
            elif u != v:
                return False
        return True


def mm(good, p, l0, l1, s):
    if l0 + l1 > len(s):
        return False
    if l0 and (not m(good, p[0], s[:l0])):
        return False
    if l1 and (not m(good, p[1], s[-l1:])):
        return False
    if l1:
        ss = s[l0:-l1]
    else:
        ss = s[l0:]
    return not good.intersection(ss)


good = set(input().strip())
pat = input().strip()
p = pat.split('*')
f = len(p) > 1
if f:
    l0 = len(p[0])
    l1 = len(p[1])
n = int(input())
for _ in range(n):
    s = input().strip()
    r = mm(good, p, l0, l1, s) if f else m(good, pat, s)
    print('YES' if r else 'NO')
