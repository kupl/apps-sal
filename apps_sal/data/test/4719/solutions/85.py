from collections import Counter

alph = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
S = [input() for _ in range(n)]
cntS = [None] * n
for i in range(n):
    cntS[i] = Counter(S[i])

ans = []
for c in alph:
    ans += [c * min(cntS[i][c] for i in range(n))]

print(''.join(ans))
