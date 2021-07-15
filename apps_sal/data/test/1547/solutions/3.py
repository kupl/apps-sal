# You lost the game.
n, m, k = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(k)]

T = [[0 for _ in range(m)] for _ in range(n)]
R = [[0,-1] for _ in range(n)]
C = [[0,-1] for _ in range(m)]

"""for i in range(n):
    for j in range(m):
        for l in range(k-1,-1,-1):
            if (Q[l][0] == 1 and Q[l][1] == i+1) or (Q[l][0] == 2 and Q[l][1] == j+1):
                T[i][j] = Q[l][2]
                break"""

for i in range(k):
    q = Q[i]
    if q[0] == 1:
        R[q[1]-1] = [q[2],i]
    else:
        C[q[1]-1] = [q[2],i]

for i in range(n):
    for j in range(m):
        if R[i][1] > C[j][1]:
            T[i][j] = R[i][0]
        else:
            T[i][j] = C[j][0]

for i in range(n):
    for j in range(m):
        print(T[i][j],end=" ")
    print()

    

