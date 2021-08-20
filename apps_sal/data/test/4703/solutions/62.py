from itertools import product
S = list(input())
N = len(S)
ans = 0
for adds in product([0, 1], repeat=N - 1):
    eqn = [''] * (2 * N - 1)
    eqn[::2] = S[:]
    for (i, has_add) in enumerate(adds):
        if has_add:
            eqn[2 * i + 1] = '+'
        else:
            eqn[2 * i + 1] = ''
    ans += eval(''.join(eqn))
print(ans)
