n, k = map(int, input().split())
favor = [tuple(input().split()) for _ in range(n)]
square = [[0 for _ in range(k)] for _ in range(k)]
initscore = 0
for xc, yc, c in favor:
    x = int(xc)
    y = int(yc)
    x %= 2*k
    y %= 2*k
    if (x in range(k) and y in range(k)) or (x in range(k, 2*k) and y in range(k, 2*k)):
        if c == 'B':
            square[x%k][y%k] += 1
        else:
            square[x%k][y%k] -= 1
            initscore += 1
    else:
        if c == 'B':
            square[x%k][y%k] -= 1
            initscore += 1
        else:
            square[x%k][y%k] += 1
cum = [[0 for _ in range(k+1)] for _ in range(k+1)]
for i in range(k):
    for j in range(k):
        cum[i+1][j+1] = cum[i+1][j] + cum[i][j+1] - cum[i][j] + square[i][j]
maxscore = 0
for i in range(k):
    for j in range(k):
        score = cum[i][k] + cum[k][j] - 2*cum[i][j]
        maxscore = max(maxscore, max(cum[k][k] - score, score))
print(maxscore + initscore)
