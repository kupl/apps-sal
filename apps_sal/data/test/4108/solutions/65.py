S = input()
T = input()
N = len(S)

chr_from = {}
chr_to = {}

flg = True

for i in range(N):
    if T[i] in chr_to:
        if S[i] not in chr_from:
            chr_to[T[i]] += 1
    else:
        chr_to[T[i]] = 1

    if S[i] in chr_from:
        if chr_from[S[i]] != T[i]:
            flg = False
    else:
        chr_from[S[i]] = T[i]

for val in chr_to.values():
    if val > 1:
        flg = False


print(['No', 'Yes'][flg])
