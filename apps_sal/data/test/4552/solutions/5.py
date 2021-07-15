n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]
ans = -float("inf")
for i in range(1, 2**10):
    tf = [False]*10
    for j in range(10):
        if (i>>j)&1:
            tf[j] = True
    cnt1 = 0
    for j in range(n):
        cnt2 = 0
        for k in range(10):
            if tf[k] and f[j][k]:
                cnt2 += 1
        cnt1 += p[j][cnt2]
    ans = max(ans, cnt1)
print(ans)
