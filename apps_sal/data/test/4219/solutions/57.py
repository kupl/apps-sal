N = int(input())

W = [[-1]*N for _ in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = [int(z) for z in input().split()]
        x -= 1
        W[i][x] = y

M = 0
for b in range(2**N):

    d = [0] * N
    for i in range(N):
        if (b >> i) & 1:
            d[i] = 1
    
    ok = True
    for i in range(N):
        if d[i] == 1:
            for j in range(N):
                if W[i][j] == -1:
                    continue
                if W[i][j] != d[j]:
                    ok =False

    if ok == True:
        M = max(M, sum(d))

print(M)
