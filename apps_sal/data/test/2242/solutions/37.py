from collections import Counter
S = input()[::-1]
MOD = 2019
X = [0]
for i,s in enumerate(S):
    X.append((X[-1]+int(s)*pow(10,i,MOD))%MOD)
C = Counter(X)
print(sum([v*(v-1)//2 for v in C.values()]))
