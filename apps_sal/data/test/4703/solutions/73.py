from itertools import product

S = input()
N = len(S)
S2 = S[0]
for i in range(N - 1):
    S2 += '{}' + S[i + 1]

ans = 0
for p in product(['', '+'], repeat=N - 1):
    ans += eval(S2.format(*p))

print(ans)
