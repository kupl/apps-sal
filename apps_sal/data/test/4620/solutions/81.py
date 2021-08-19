N = int(input())
C = [0] * (N - 1)
S = [0] * (N - 1)
F = [0] * (N - 1)
for TN in range(0, N - 1):
    (C[TN], S[TN], F[TN]) = (int(T) for T in input().split())
for TN in range(0, N):
    Time = 0
    for TS in range(TN, N - 1):
        if Time >= S[TS]:
            Time += C[TS] + (F[TS] - Time % F[TS]) % F[TS]
        else:
            Time += C[TS] + (S[TS] - Time)
    print(Time)
