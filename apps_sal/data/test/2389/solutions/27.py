N, A, B, C = list(map(int, input().split()))
X = [A, B, C]
ANS = []

flg = True
D = []
pat = {'AB': [0, 1], 'BC': [1, 2], 'AC': [0, 2]}

for i in range(N):
    l = input()
    D.append(pat[l])

for i in range(N):
    ai, bi = D[i]
    an, bn = D[i + 1] if i < N - 1 else [0, 1]

    if X[ai] == 0 and X[bi] == 0:
        flg = False
        break
    elif X[ai] == 0:
        ANS.append(ai)
        X[ai] += 1
        X[bi] -= 1
    elif X[bi] == 0:
        ANS.append(bi)
        X[bi] += 1
        X[ai] -= 1
    else:
        if ai == an or ai == bn:
            pl, mi = ai, bi
        else:
            pl, mi = bi, ai
        ANS.append(pl)
        X[pl] += 1
        X[mi] -= 1

if not flg:
    print('No')
else:
    print('Yes')
    dd = {0: 'A', 1: 'B', 2: 'C'}
    for ans in ANS:
        print((dd[ans]))
