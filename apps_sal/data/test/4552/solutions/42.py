from itertools import combinations

n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = - 10 ** 18
for i in range(1, 11):
    for pat in combinations(list(range(10)), i):
        cnt = [0] * n
        for e in pat:
            for j in range(n):
                cnt[j] += f[j][e]

        score = 0
        for i, e in enumerate(cnt):
            score += p[i][e]

        ans = max(ans, score)

print(ans)
