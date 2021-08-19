(N, K) = (int(T) for T in input().split())
Reminder = [0] * K
for NT in range(1, N + 1):
    Reminder[NT % K] += 1
Count = 0
for RA in range(0, K):
    RB = (K - RA) % K
    RC = (K - RA) % K
    if (RB + RC) % K == 0:
        Count += Reminder[RA] * Reminder[RB] * Reminder[RC]
print(Count)
