import sys

input = sys.stdin.readline
N, M = map(int, input().split())
scores = []
for _ in range(N):
    x, y, z = map(int, input().split())
    scores.append((x, y, z))

ans = 0
for i in range(2**3):
    tmp_scores = []
    for score in scores:
        tmp_score = 0
        for j in range(3):
            if (i >> j) & 1:
                tmp_score -= score[j]
            else:
                tmp_score += score[j]
        tmp_scores.append(tmp_score)
    tmp_scores.sort(reverse=True)
    ans = max(ans, sum(tmp_scores[:M]))

print(ans)
