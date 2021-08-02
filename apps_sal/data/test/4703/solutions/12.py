import itertools as it
import copy
S = input()
l = len(S)
ls = ''
for i in range(1, l): ls += str(i)
sa = [''] * (2 * l - 1)
for i in range(len(sa)):
    if i % 2 == 0:
        sa[i] = S[i // 2]

ans = 0
for i in range(l):
    for j in list(it.combinations(ls, i)):
        sx = copy.copy(sa)
        for k in j:
            k = int(k)
            sx[2 * k - 1] = '+'
        ans += eval(''.join(sx))
print(ans)
