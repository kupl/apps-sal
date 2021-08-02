n, T = list(map(int, input().split()))
A = list(map(int, input().split()))

AIND = [(A[i], i) for i in range(n)]
AS = sorted(AIND)
MINA = AS[0][0]

SUM = [AS[0][0]]
for i in range(1, n):
    SUM.append(AS[i][0] + SUM[-1])

SUM.reverse()
AS.reverse()
MAX = SUM[0]
x = 0

ANS = 0

# print(AIND,AS,MINA,SUM,MAX)

while T >= MINA:
    if T > SUM[x]:
        ANS += (n - x) * (T // SUM[x])
        T = T % SUM[x]

    else:
        if T < AS[x][0]:
            x += 1
        else:
            for i in range(n):
                if T >= A[i]:
                    T -= A[i]
                    ANS += 1


print(ANS)
