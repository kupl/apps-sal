n = int(input())

l = [[c for c in input()] for _ in range(n)]

ok = False
for r in l:
    if r[0] == r[1] == 'O':
        r[0] = r[1] = '+'
        ok = True
        break
    if r[3] == r[4] == 'O':
        r[3] = r[4] = '+'
        ok = True
        break

if ok:
    print('YES')
    for r in l:
        print(''.join(r))
else:
    print('NO')
