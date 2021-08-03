n = int(input())

L, score = [], []
for i in range(n):
    L.append(list(map(int, input().split())))

for i in range(n):
    score.append(list(map(int, input().split())))

ans = -10**32

for k in range(1, 1 << 10):
    sc = 0

    for i in range(n):
        cnt = 0
        for j in range(10):
            if L[i][j] and k >> j & 1:
                cnt += 1
        # print(L[i],v,cnt,i,score,score[i][cnt])
        sc += score[i][cnt]
        # print(L[i],v,cnt,i,score,score[i][cnt])
    ans = max(ans, sc)

print(ans)
