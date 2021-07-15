N = int(input())
W = list(map(int, input().split()))

S1, S2 = 0, 0
lists = []

for T in range(1, N):
    for T_low in range(0, T):
        S1 += W[T_low]
    for T_high in range(T, N):
        S2 += W[T_high]

    lists.append(abs(S1 - S2))
    S1, S2 = 0, 0

print(min(lists))
