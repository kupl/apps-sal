# You lost the game.

n = int(input())
C = [list(map(int, input().split())) for i in range(n)]

L = sum([C[i][0] for i in range(n)])
R = sum([C[i][1] for i in range(n)])

if 1:
    ml = 0
    mr = 0
    ind1 = -1
    ind2 = -1
    for i in range(n):
        if C[i][1] - C[i][0] > ml:
            ml = C[i][1] - C[i][0]
            ind1 = i
        elif C[i][0] - C[i][1] > mr:
            mr = C[i][0] - C[i][1]
            ind2 = i

D = abs(L - R)
D1 = abs((L + C[ind1][1] - C[ind1][0]) - (R + C[ind1][0] - C[ind1][1]))
D2 = abs((L + C[ind2][1] - C[ind2][0]) - (R + C[ind2][0] - C[ind2][1]))

if D1 > D2 and D2 > D:
    print(1 + ind1)
elif D2 > D1 and D1 > D:
    print(1 + ind2)
elif D2 > D:
    print(1 + ind2)
elif D1 > D:
    print(1 + ind1)
else:
    print(0)
