(n, k) = map(int, input().split())
ns = {}
for c in input():
    if c in ns.keys():
        ns[c] += 1
    else:
        ns[c] = 1
for a in ns.values():
    if a > k:
        print('NO')
        break
else:
    print('YES')
