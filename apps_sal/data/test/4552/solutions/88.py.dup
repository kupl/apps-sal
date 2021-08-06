import itertools
n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
ans = -(10**12)
for i in range(1, 11):
    num = list(itertools.combinations(list(range(10)), i))
    for j in range(len(num)):
        cnt = [0] * n
        cnt2 = 0
        for k in range(i):
            for l in range(n):
                if f[l][num[j][k]] == 1:
                    cnt[l] += 1
        for k in range(n):
            cnt2 += p[k][cnt[k]]
        ans = max(cnt2, ans)
print(ans)
