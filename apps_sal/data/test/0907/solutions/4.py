n, m = list(map(int, input().split()))
pairs = [tuple(int(x) for x in input().split()) for _ in range(m)]

possible = {pairs[0], (pairs[0][0], None), (pairs[0][1], None)}
for p in pairs[1:]:
    add = set()
    remove = set()
    for o in possible:
        if p[0] in o or p[1] in o:
            continue
        remove.add(o)
        if o[1] is None:
            add.add((o[0], p[0]))
            add.add((o[0], p[1]))
    possible = (possible - remove) | add
    if not possible:
        break

if not possible:
    print('NO')
else:
    print('YES')
