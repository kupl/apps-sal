N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.append(A[0])
B.append(B[0])
AX = []
BX = []
for i in range(N):
    AX.append(A[i] ^ A[i + 1])
    BX.append(B[i] ^ B[i + 1])
AX += AX[:-1]
LEN = len(BX)
MP = [-1] * (LEN + 1)
NOW = -1
for i in range(LEN):
    while NOW >= 0 and BX[i] != BX[NOW]:
        NOW = MP[NOW]
    NOW += 1
    MP[i + 1] = NOW
LEN2 = len(AX)
MP_SEARCH = [0] * LEN2
NOW = 0
for i in range(LEN2):
    while NOW >= 0 and AX[i] != BX[NOW]:
        NOW = MP[NOW]
    NOW += 1
    MP_SEARCH[i] = NOW
    if NOW == LEN:
        NOW = MP[NOW]
for i in range(LEN2):
    if MP_SEARCH[i] == LEN:
        print(i - LEN + 1, A[i - LEN + 1] ^ B[0])
