# You lost the game.
r,c,n,k = list(map(int, input().split()))
V = [list(map(int, input().split())) for _ in range(n)]

G = [[0 for _ in range(c)] for _ in range(r)]
for i in range(n):
    G[V[i][0]-1][V[i][1]-1] = 1


T = [[0 for _ in range(c)] for _ in range(r)]
T[0][0] = G[0][0]
for i in range(1,r):
    T[i][0] = G[i][0]
for i in range(r):
    for j in range(1,c):
        T[i][j] = T[i][j-1] + G[i][j]
for i in range(1,r):
    for j in range(c):
        T[i][j] += T[i-1][j]
nb = 0
for x1 in range(c):
    for x2 in range(x1,c):
        for y1 in range(r):
            for y2 in range(y1,r):
                s = T[y2][x2]
                if x1 > 0:
                    s -= T[y2][x1-1]
                if y1 > 0:
                    s -= T[y1-1][x2]
                if x1 > 0 and y1 > 0:
                    s += T[y1-1][x1-1]
                if s >= k:
                    nb += 1
print(nb)

