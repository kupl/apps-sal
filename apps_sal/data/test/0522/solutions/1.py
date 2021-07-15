N, f1, f2, f3, x = list(map(int, input().split()))
def mmult(A, B):
    nonlocal mod
    n, m, l = len(A), len(B), len(B[0])
    ret = [[0]*l for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                ret[i][k] = (ret[i][k]+A[i][j]*B[j][k])%mod
    return ret
def mpow(A, n):
    if n == 1:
        return A
    if n % 2:
        return mmult(mpow(A, n-1), A)
    return mpow(mmult(A, A), n//2)
P = 10**9+7
mod = P - 1
X = [[1,1,0],[1,0,1],[1,0,0]]
Y = [[1,1,0,0,0],[1,0,1,0,0],[1,0,0,0,0],[1,0,0,1,0],[1,0,0,1,1]]
a = 0 if N == 4 else mmult([[1,0,0]], mpow(X,N-4))[0][0]%mod
b = mmult([[0,1,0]], mpow(X,N-3))[0][0]%mod
c = mmult([[0,0,1]], mpow(X,N-2))[0][0]%mod
d = mmult([[0,0,0,0,1]], mpow(Y,N-3))[0][0]%mod
print(pow(f1, a, P)*pow(f2, b, P)*pow(f3, c, P)*pow(x*x, d, P)%P)

