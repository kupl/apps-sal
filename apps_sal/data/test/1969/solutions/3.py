n = int(input())
M = [input() for i in range(n)]

ANS = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if M[i][j] == M[i - 1][j - 1] == M[i - 1][j + 1] == M[i + 1][j - 1] == M[i + 1][j + 1] == "X":
            ANS += 1

print(ANS)
