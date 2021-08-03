N = int(input())
S = []
P = []
for i in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))
Sset = sorted(list(set(S)))

dict1 = {}
for i in range(N):
    dict1[P[i]] = S[i]

for k in Sset:
    U = [i for i, j in dict1.items() if j == k]
    V = sorted(U, reverse=True)
    for l in V:
        print(P.index(l) + 1)
