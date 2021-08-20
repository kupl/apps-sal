import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    (n, m) = list(map(int, input().split()))
    S = input().strip()
    P = list(map(int, input().split()))
    SCORE = [[0] * 26 for i in range(n)]
    for i in range(n):
        for j in range(26):
            SCORE[i][j] = SCORE[i - 1][j]
        SCORE[i][ord(S[i]) - 97] += 1
    ANS = [0] * 26
    for p in P:
        for j in range(26):
            ANS[j] += SCORE[p - 1][j]
    for j in range(26):
        ANS[j] += SCORE[-1][j]
    print(*ANS)
