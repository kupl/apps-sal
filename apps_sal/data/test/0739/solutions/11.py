import numpy as np

L, A, B, M = map(int, input().split())

def dot(A, B, mod):
    r = len(A)
    c = len(B[0])
    m = len(A[0])
    res = [[0] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            for k in range(m):
                res[i][j] += A[i][k] * B[k][j] % mod
                res[i][j] %= mod
    
    return res

def rec_pow(k, n, mod):
    if n == 1:
        return k
    
    k2 = dot(k, k, mod)
    if n % 2 ==0:
        return rec_pow(k2, n//2, mod)
    else:
        return dot(rec_pow(k2, n//2, mod), k, mod)

s = [[0, A%M, 1]]

for d in range(1, 19):
    n1 = min(max(0, (10**d-1-A)//B+1), L)
    n0 = min(max(0, (10**(d-1)-1-A)//B+1), L)
    n = n1 - n0
    if n == 0:
        continue
        
    k = [[pow(10, d, M), 0, 0], [1, 1, 0], [0, B%M, 1]]
    
    s = dot(s, rec_pow(k, n, M), M)
    
    if n1 >= L:
        break
        
print(s[0][0])
