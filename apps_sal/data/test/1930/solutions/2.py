import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))
mod = 998244353

INV = [None] * (n + 1)  # 1/aのリストを予め作っておく.
for i in range(1, n + 1):
    INV[i] = pow(i, mod - 2, mod)

BLA = P.count(-1)

if BLA == 0 or BLA == 1:
    ANS = 0
else:
    LEFT = BLA * (BLA - 1) // 2 * INV[BLA] % mod  # 左側の個数の平均
    AVEP = BLA * (BLA - 1) // 2 * pow(BLA - 1, mod - 2, mod)  # 左側にあるものが自分より大きい確率の和

    ANS = LEFT * AVEP % mod


# print(ANS,LEFT,AVEP)
y = 1
for i in range(BLA):
    y = y * (BLA - i) % mod

KOSUU = pow(y, mod - 2, mod)
BLALIST = [1] * (n + 1)
NONBLA = []
BLANUM = [0] * n
for i in range(n):
    if P[i] != -1:
        BLALIST[P[i]] = 0
        BLANUM[i] = BLANUM[i - 1]
        NONBLA.append(P[i])

    else:
        BLANUM[i] = BLANUM[i - 1] + 1

# print(BLALIST)
BLALIST[0] = 0
for i in range(1, n + 1):
    BLALIST[i] = BLALIST[i - 1] + BLALIST[i]

if BLA != 0:
    for i in range(n):
        if P[i] != -1:
            ANS = (ANS + (BLANUM[i] * (BLA - BLALIST[P[i]]) + (BLA - BLANUM[i]) * BLALIST[P[i]]) * INV[BLA]) % mod

# print(ANS)

A = NONBLA

if A == []:
    print(ANS)
    return


n = len(A)
MAXA = max(A)
MINA = min(A)


BIT = [0] * (MAXA - MINA + 2)  # 出現回数をbit indexed treeの形でもっておく.

for i in range(n):  # A[0],A[1],...とBITを更新
    bitobje = A[i] - MINA + 1

    x = bitobje
    while x != 0:
        ANS = (ANS - BIT[x]) % mod
        x -= (x & (-x))

    # print(ANS)

    x2 = MAXA - MINA + 1
    # print(x2)
    while x2 != 0:
        # print(x2,BIT)
        ANS = (ANS + BIT[x2]) % mod
        x2 -= (x2 & (-x2))

    # print(ANS)

    y = bitobje
    while y <= MAXA - MINA + 1:
        BIT[y] += 1
        y += (y & (-y))

    # print(ANS,BIT)

print(ANS)
