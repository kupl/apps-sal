s = input()
t = input()
ls = len(s)
lt = len(t)

ans = 0
for i in range(ls - lt + 1):
    x = s[:i] + t + s[i + lt:ls]
    f = 1
    for j in range(ls):
        if s[j] == '?':
            continue
        if s[j] != x[j]:
            f = 0
            break
    if f:
        p = ''
        for k in range(ls):
            if x[k] == '?':
                p += 'a'
            else:
                p += x[k]
        ans = p

if ans:
    print(p)
else:
    print('UNRESTORABLE')
