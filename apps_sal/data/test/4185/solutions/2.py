import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

CR = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        CR[i][j] -= 1

MAX = n * m
ANS = 0

for i in range(m):
    SCORE = [0] * n

    for j in range(n):
        if CR[j][i] % m == i % m and 0 <= CR[j][i] < MAX:
            x = (CR[j][i] - i % m) // m
            SCORE[(j - x) % n] += 1

        # print(SCORE)

    # print(SCORE)

    ANS += min([n + j - SCORE[j] for j in range(n)])

print(ANS)
