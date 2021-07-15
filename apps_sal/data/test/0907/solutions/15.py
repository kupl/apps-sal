n, m = list(map(int, input().split()))
if m <= 2:
    print('YES')
    return
a = list({frozenset(list(map(int, input().split()))) for q in range(m)})
x = list(a[0])[0]
y = list(a[0]-{x})[0]
s = set()
for q in a:
    if x not in q:
        s.add(q)
if len(s) < 2:
    print('YES')
    return
s = iter(s)
x = set(next(s)) & next(s)
if len(x) != 0:
    x = list(x)[0]
    for q in s:
        if x not in q:
            break
    else:
        print('YES')
        return
s = set()
for q in a:
    if y not in q:
        s.add(q)
if len(s) < 2:
    print('YES')
    return
s = iter(s)
y = set(next(s)) & next(s)
if len(y) == 0:
    print('NO')
    return
y = list(y)[0]
for q in s:
    if y not in q:
        print('NO')
        break
else:
    print('YES')

