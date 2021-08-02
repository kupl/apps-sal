n = int(input())
fl = [list(map(int, input().split())) for _ in range(n)]
pl = [list(map(int, input().split())) for _ in range(n)]

ans = -1001001001
for i in range(1, 2**10):
    profit = 0
    cnt = [0] * n
    for j in range(10):
        if (i >> j) & 1 == 1:
            for k in range(n):
                if fl[k][j] == 1:
                    cnt[k] += 1
    for k in range(n):
        profit += pl[k][cnt[k]]
    ans = max(ans, profit)

print(ans)
