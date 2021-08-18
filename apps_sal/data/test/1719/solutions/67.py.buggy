n = int(input())
if n == 3:
    print((61))
    return
mod = pow(10, 9) + 7
# d={'A':0,'G':1,'C':2,'T':3}
d = {0: 'A', 1: 'G', 2: 'C', 3: 'T'}
dd = {}
dinitial = {}
for i in range(4**4):
    key = []
    for _ in range(4):
        key.append(d[i % 4])
        i //= 4
    key = ''.join(key)
    if 'AGC' in key:
        continue
    if 'ACG' in key:
        continue
    if 'GAC' in key:
        continue
    if key[0] == 'A' and key[2:4] == 'GC':
        continue
    if key[0:2] == 'AG' and key[3] == 'C':
        continue
    dd[key] = 1
    dinitial[key] = 0

for _ in range(n - 4):
    ddd = dinitial.copy()
    for k in dd:
        if k[1:] + 'A' in ddd:
            ddd[k[1:] + 'A'] += dd[k]
            ddd[k[1:] + 'A'] %= mod
        if k[1:] + 'G' in ddd:
            ddd[k[1:] + 'G'] += dd[k]
            ddd[k[1:] + 'G'] %= mod
        if k[1:] + 'C' in ddd:
            ddd[k[1:] + 'C'] += dd[k]
            ddd[k[1:] + 'C'] %= mod
        if k[1:] + 'T' in ddd:
            ddd[k[1:] + 'T'] += dd[k]
            ddd[k[1:] + 'T'] %= mod
    dd = ddd

print((sum(dd.values()) % mod))
