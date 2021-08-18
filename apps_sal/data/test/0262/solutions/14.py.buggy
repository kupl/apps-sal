from sys import stdin

n = int(stdin.readline())
carre = [list(map(int, stdin.readline().split())) for i in range(n)]
sommesCol = [0] * n
sommesLig = [0] * n
if n == 1:
    print(1)
    return

for lig in range(n):
    for col in range(n):
        if carre[lig][col] == 0:
            ligManque = lig
            colManque = col
        else:
            sommesCol[col] += carre[lig][col]
            sommesLig[lig] += carre[lig][col]

sommeDiagonale = 0
sommeDiagonaleInv = 0
for i in range(n):
    sommeDiagonale += carre[i][i]
    sommeDiagonaleInv += carre[i][n - i - 1]
reference = sommesCol[(colManque + 1) % n]
remplacement = reference - sommesCol[colManque]

sommesCol[colManque] += remplacement
sommesLig[ligManque] += remplacement
if ligManque == colManque:
    sommeDiagonale += remplacement
if ligManque == n - colManque - 1:
    sommeDiagonaleInv += remplacement

possible = True
if sommeDiagonale != reference:
    possible = False
if sommeDiagonaleInv != reference:
    possible = False
for col in range(n):
    if sommesCol[col] != reference:
        possible = False
for lig in range(n):
    if sommesLig[lig] != reference:
        possible = False

if not possible or remplacement <= 0:
    print(-1)
else:
    print(remplacement)
