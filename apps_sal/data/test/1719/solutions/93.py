n = int(input())
mod = 10 ** 9 + 7
A = [1] + [0] * (n - 1)
G = [1] + [0] * (n - 1)
T = [1] + [0] * (n - 1)
C = [1] + [0] * (n - 1)
AG = [0] * n
GA = [0] * n
AC = [0] * n
AGG = [0] * n
AGT = [0] * n
ATG = [0] * n
for i in range(1, n):
    tmp = A[i - 1] + G[i - 1] + C[i - 1] + T[i - 1]
    A[i] = tmp % mod
    T[i] = tmp % mod
    G[i] = (tmp - AC[i - 1]) % mod
    C[i] = (tmp - AG[i - 1] - GA[i - 1] - AGG[i - 1] - AGT[i - 1] - ATG[i - 1]) % mod
    AG[i] = A[i - 1]
    GA[i] = G[i - 1]
    AC[i] = (A[i - 1] - GA[i - 1]) % mod
    AGG[i] = AG[i - 1]
    AGT[i] = AG[i - 1]
    ATG[i] = A[i - 2]
print((A[-1] + G[-1] + C[-1] + T[-1]) % mod)
