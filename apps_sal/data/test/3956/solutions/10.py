(K, N) = list(map(int, input().split()))
mod = 998244353
INV = [None] * (N + K + 2)
for i in range(1, N + K + 2):
    INV[i] = pow(i, mod - 2, mod)
Combi = [None] * (N + K + 1)
Combi[K - 1] = 1
for i in range(K, N + K + 1):
    Combi[i] = Combi[i - 1] * i * INV[i - K + 1] % mod
all = Combi[N + K - 1]
ANSLIST = []
for i in range(2, 2 + K):
    ANS = all
    x = i // 2 - max(0, i - K - 1)
    CB_x = 1
    j = 1
    while N + K - 1 - j * 2 >= K - 1 and j <= x:
        CB_x = CB_x * (x - j + 1) // j
        ANS += (-1) ** j * CB_x * Combi[N + K - 1 - j * 2]
        ANS = ANS % mod
        j += 1
    ANSLIST.append(ANS % mod)
for i in ANSLIST:
    print(i)
ANSLIST = ANSLIST[::-1]
for j in ANSLIST[1:]:
    print(j)
