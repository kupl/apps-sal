from collections import Counter
(n, m) = list(map(int, input().split()))
f = list(map(int, input().split()))
b = list(map(int, input().split()))
(ctf, ctb) = (Counter(f), Counter(b))
possible = True
ambiguous = False
for (k, v) in list(ctb.items()):
    if k not in ctf:
        possible = False
    if ctf[k] >= 2:
        ambiguous = True
idx = {}
for (i, v) in enumerate(f):
    idx[v] = i + 1
if not possible:
    print('Impossible')
elif ambiguous:
    print('Ambiguity')
else:
    print('Possible')
    a = []
    for v in b:
        a.append(idx[v])
    print(' '.join(map(str, a)))
