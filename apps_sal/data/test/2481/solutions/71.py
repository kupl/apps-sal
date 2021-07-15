H, W = map(int, input().split())
C = []
N = 10
for i in range(N):
    c = list(map(int, input().split()))
    C.append(c)

def w_f(C):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                C[i][j] = min(C[i][j], C[i][k]+C[k][j])
    return C

C = w_f(C)

A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] != -1:
            ans += C[A[h][w]][1]
            
print(ans)
