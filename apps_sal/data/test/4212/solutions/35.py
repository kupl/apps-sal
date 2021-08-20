from itertools import combinations_with_replacement as cwr
(N, M, Q) = map(int, input().split())
ABCD = []
for _ in range(Q):
    ABCD.append(list(map(int, input().split())))
maxscore = 0
for comb in cwr(range(1, M + 1), N):
    score = 0
    for row in ABCD:
        if comb[row[1] - 1] - comb[row[0] - 1] == row[2]:
            score += row[3]
    maxscore = max(maxscore, score)
print(maxscore)
