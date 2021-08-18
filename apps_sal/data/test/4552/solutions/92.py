N = int(input())

F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -float("inf")

for i in range(1, 2**10):
    score = 0
    jonson = [0 for _ in range(10)]

    for j in range(10):
        if ((i >> j) & 1):
            jonson[j] = 1
    for k in range(N):
        cnt = 0
        for l in range(10):
            if F[k][l] == jonson[l] == 1:
                cnt += 1
        score += P[k][cnt]

    ans = max(score, ans)

print(ans)
