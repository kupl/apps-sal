N, C = list(map(int,input().split()))
D = [list(map(int,input().split())) for _ in range(C)]
G = [list(map(int,input().split())) for _ in range(N)]
Z = [0]*C
O = [0]*C
T = [0]*C
for x in range(N):
    for y in range(N):
        if (x+y)%3 == 0:
            Z[G[x][y]-1] += 1
        elif (x+y)%3 == 1:
            O[G[x][y]-1] += 1
        else:
            T[G[x][y]-1] += 1

ans = 10**9
for c1 in range(C):
    for c2 in range(C):
        for c3 in range(C):
            if c1 == c2 or c2 == c3 or c3 == c1:
                continue
            temp = 0
            for k in range(C):
                temp += Z[k]*D[k][c1]
            for k in range(C):
                temp += O[k]*D[k][c2]
            for k in range(C):
                temp += T[k]*D[k][c3]
            ans = min(ans,temp)

print(ans)

