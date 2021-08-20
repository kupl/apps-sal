n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]
ans = -(1 << 30)
for bit in range(1, 1 << 10):
    cnt = 0
    for i in range(n):
        cnt2 = 0
        for j in range(10):
            if bit >> j & 1 and f[i][j]:
                cnt2 += 1
        cnt += p[i][cnt2]
    if ans < cnt:
        ans = cnt
print(ans)
