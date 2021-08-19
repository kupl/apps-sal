from collections import Counter


def PowerMod(N, P, Mod):
    if N % Mod == 0:
        return 0
    else:
        PowM = 1
        for TP in range(1, P + 1):
            PowM = PowM * N % Mod
        return PowM


N = int(input())
A = sorted(Counter([int(T) for T in input().split()]).most_common(), key=lambda X: X[0])
PassFlag = True
if N % 2 == 1:
    for TA in range(0, (N + 1) // 2):
        if A[TA][0] != 2 * TA or A[TA][1] != 1 + (A[TA][0] != 0):
            PassFlag = False
            break
    print([0, PowerMod(2, (N - 1) // 2, 10 ** 9 + 7)][PassFlag])
else:
    for TA in range(0, N // 2):
        if A[TA][0] != 2 * TA + 1 or A[TA][1] != 2:
            PassFlag = False
            break
    print([0, PowerMod(2, N // 2, 10 ** 9 + 7)][PassFlag])
