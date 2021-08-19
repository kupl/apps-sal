N = int(input())
P = map(int, input().split())
S = []
for (x, y) in zip(P, range(1, N + 1)):
    if x == y:
        S.append(y)
S.append('$')
L = len(S)
lake = []
lake.append(S[0])
i = 1
a = 0
while i < L:
    if S[i] == '$':
        a += 1
    elif lake[0] + 1 != S[i]:
        a += 1
        lake = []
        lake.append(S[i])
    else:
        lake.append(S[i])
    i += 1
print(a)
