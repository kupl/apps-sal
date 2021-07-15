import sys
readline = sys.stdin.readline

def mat_dot(A, B, mod):
    assert len(A[0]) == len(B), 'invalid_size'
    
    L = len(A)
    M = len(A[0])
    N = len(B[0])
    
    res = [[0]*N for _ in range(L)]
    
    for i in range(L):
        for j in range(N):
            a = 0
            for k in range(M):
                a = (a+A[i][k]*B[k][j]) % mod
            res[i][j] = a
            
    return res

def mat_pow(A, x, mod):
    N = len(A)
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1
    for i in range(x.bit_length()):
        if 2**i & x:
            res = mat_dot(res, A, mod)
        A = mat_dot(A, A, mod)
    return res

MOD = 998244353 
N, M, L, R = map(int, readline().split())
R -= L
if N&1 and M&1:
    ans = pow(R+1, N*M, MOD)
else:
    Bl = N*M//2
    even = (R+1)//2
    odd = R+1 - even
    Mat = [[even, odd], [odd, even]]
    xy = mat_dot(mat_pow(Mat, Bl, MOD), [[1], [0]], MOD)
    x, y = xy[0][0], xy[1][0]
    ans = (x*x + y*y) % MOD
    
print(ans)
