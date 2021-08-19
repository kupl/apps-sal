import collections
n = int(input())
lsp = list(map(int, input().split()))
lse = []
lso = []
for i in range(n):
    if i % 2 == 0:
        lse.append(lsp[i])
    else:
        lso.append(lsp[i])
countere = collections.Counter(lse)
countero = collections.Counter(lso)
valuee = sorted(list(countere.values()), reverse=True) + [0]
valueo = sorted(list(countero.values()), reverse=True) + [0]
keyse = []
for i in countere.keys():
    if countere[i] == valuee[0]:
        keyse.append(i)
keyso = []
for i in countero.keys():
    if countero[i] == valueo[0]:
        keyso.append(i)
factor = 0
if len(keyse) == 1 and len(keyso) == 1 and (keyso == keyse):
    factor = min(valuee[0] - valuee[1], valueo[0] - valueo[1])
print(n - valuee[0] - valueo[0] + factor)
