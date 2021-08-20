import math
N = int(input())
T = [0] * N
for i in range(N):
    T[i] = int(input())
if N == 1:
    print(T[0])
elif N == 2:
    print(T[0] * T[1] // math.gcd(T[0], T[1]))
else:
    L = T[0]
    for i in range(1, N):
        L = L * T[i] // math.gcd(L, T[i])
    print(L)
