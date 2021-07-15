from collections import Counter
N = int(input())
Aset = dict()
Ans = 0
for _ in range(N):
    S = input()
    NewS = ''
    S = sorted(S)
    for i in range(len(S)):
        NewS += S[i]
    if NewS not in Aset:
        Aset[NewS] = 1
    else:
        Ans += Aset[NewS]
        Aset[NewS] += 1
print(Ans)
