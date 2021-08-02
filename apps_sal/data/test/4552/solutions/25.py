n = int(input())

f = []
for i in range(n):
    f.append(list(map(int, input().split())))
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

ans = -10**18
for ci in range(1, 2**10):
    score = 0
    for cn in range(n):
        cnt = 0
        for cj in range(10):
            x = ci >> cj & 1
            if x and f[cn][cj]:
                cnt += 1
        score += p[cn][cnt]
    ans = max(ans, score)
print(ans)
