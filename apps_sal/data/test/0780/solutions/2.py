from collections import Counter
s = input().strip()
C = Counter()
for i in range(1, len(s)):
    if int(s[i]) >= int(s[i - 1]):
        C[int(s[i]) - int(s[i - 1])] += 1
    else:
        C[int(s[i]) + 10 - int(s[i - 1])] += 1
NEED = [[[10000] * 10 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(13):
            for l in range(13):
                if k + l == 0:
                    continue
                NEED[i][j][(i * k + j * l) % 10] = min(k + l, NEED[i][j][(i * k + j * l) % 10])
for i in range(10):
    for j in range(10):
        ANS = 0
        for c in C:
            if NEED[i][j][c] == 10000:
                ANS = -1
                break
            else:
                ANS += (NEED[i][j][c] - 1) * C[c]
        print(ANS, end=' ')
    print()
