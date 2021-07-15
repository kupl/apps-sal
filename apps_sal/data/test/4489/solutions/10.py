from collections import Counter
N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

S = Counter(s)
T = Counter(t)

for key, value in list(S.items()):
    if key in list(T.keys()):
        S[key] -= T[key]

if max(S.values()) > 0:
    print((max(S.values())))
else:
    print((0))


