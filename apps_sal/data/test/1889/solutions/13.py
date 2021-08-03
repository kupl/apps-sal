from io import StringIO

import sys
data = sys.stdin


def score_line(row):
    score = 0
    max_score = 0
    combo = False
    for b in row:
        if b == 1:
            if combo:
                score += 1
            else:
                score = 1
                combo = True
        else:
            score = 0
            combo = False

        max_score = max(score, max_score)
    return max_score


rows = []

n, m, q = map(int, data.readline().split(' '))
for i in range(n):
    rows.append(list(map(int, data.readline().split(' '))))

row_scores = list(map(score_line, rows))

for i in range(q):
    r, c = map(int, data.readline().split(' '))
    rows[r - 1][c - 1] = 1 - rows[r - 1][c - 1]
    row_scores[r - 1] = score_line(rows[r - 1])
    print(max(row_scores))
