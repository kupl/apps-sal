(N, M) = map(int, input().split())
Stlist = [1] * N
for i in range(M):
    breakstair = int(input())
    Stlist[breakstair - 1] = 0
Comb = [1, 2]
if N == 1:
    Comb = Stlist
else:
    if Stlist[0] == 0:
        Comb[0] = 0
        Comb[1] = 1
    if Stlist[1] == 0:
        Comb[1] = 0
    for i in range(2, N):
        Comb.append((Comb[i - 1] + Comb[i - 2]) % (10 ** 9 + 7))
        if Stlist[i] == 0:
            Comb[i] = 0
print(Comb[-1])
