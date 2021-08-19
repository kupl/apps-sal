from itertools import groupby as gb
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if s.count('10') == 0:
        print(s)
        continue
    res = ''
    suf = ''
    l = [(k, len(list(v))) for (k, v) in gb(s)]
    if len(l) > 0 and l[0][0] == '0':
        res += l[0][0] * l[0][1]
        l = l[1:]
    if len(l) > 0 and l[-1][0] == '1':
        suf = l[-1][0] * l[-1][1]
        l = l[:-1]
    print(res + '0' + suf)
