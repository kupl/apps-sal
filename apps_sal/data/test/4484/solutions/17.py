import math


def ModFact(N, Mod):
    Num = 1
    for T in range(2, N + 1):
        Num = (Num * T) % Mod
    return Num


N, M = (int(T) for T in input().split())
Mod = 10**9 + 7
if N == M:
    print((2 * ModFact(N, Mod) * ModFact(M, Mod)) % Mod)
elif N == M + 1 or M == N + 1:
    print((ModFact(N, Mod) * ModFact(M, Mod)) % Mod)
else:
    print(0)
