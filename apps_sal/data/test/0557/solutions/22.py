n, m = [int(x) for x in input().split()]

tps = []
for _ in range(n):
    tps.append(tuple([int(x) for x in input().split()]))

parts = [False for _ in range(m)]
for tp in tps:
    for i in range(tp[0], tp[1]):
        parts[i] = True
for p in parts:
    if not p:
        print('NO')
        break
else:
    print('YES')
