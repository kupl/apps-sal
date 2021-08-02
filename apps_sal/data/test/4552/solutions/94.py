import itertools

N = int(input())
M = 10
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -10 ** 10
for s in itertools.product([0, 1], repeat=M):
    if max(s) == 0:
        continue
    score = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if s[j] and F[i][j]:
                cnt += 1
        score += P[i][cnt]
    ans = max(ans, score)
print(ans)
