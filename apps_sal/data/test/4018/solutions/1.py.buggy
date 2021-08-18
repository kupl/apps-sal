import sys
input = sys.stdin.readline

n, W = list(map(int, input().split()))
s = input().strip()

NEXTLIST = [[n] * 26 for i in range(n + 1)]

for i in range(n - 1, -1, -1):
    for j in range(26):
        NEXTLIST[i][j] = NEXTLIST[i + 1][j]
    NEXTLIST[i][ord(s[i]) - 97] = i

DP = [[0] * (n + 1) for i in range(n + 1)]

DP[0][0] = 1

for i in range(n):
    for j in range(26):
        if NEXTLIST[i][j] != n:
            for k in range(n):
                DP[NEXTLIST[i][j] + 1][k + 1] += DP[i][k]

# print(DP)

HLIST = [0] * (n + 1)

for i in range(n + 1):
    for j in range(n + 1):
        HLIST[j] += DP[i][j]

# print(HLIST)

ANS = 0
for i in range(n, -1, -1):
    # print(i,W)
    if W > HLIST[i]:
        ANS += (n - i) * HLIST[i]
        W -= HLIST[i]
    else:
        ANS += W * (n - i)
        print(ANS)
        return

else:
    print(-1)
