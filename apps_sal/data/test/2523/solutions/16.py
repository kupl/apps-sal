from itertools import groupby
S = input()
N = len(S)
G = [len(list(l)) for _, l in groupby(S)]
A = 0
for g in G:
    A += g
    if A >= (N+1) // 2:
        ans = min(A, N-A+g)
        print(ans)
        break
