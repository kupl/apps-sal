H, W = [int(x) for x in input().split()]
N = int(input())
a = [0] + [int(x) for x in input().split()]

ans = [[0 for _ in range(W)] for _ in range(H)]
c = 1  # 色
n = 0  # c色で塗られた数
for i in range(H):
    if i % 2 == 0:
        start = 0
        end = W
        by = 1
    else:
        start = W - 1
        end = -1
        by = -1
    for j in range(start, end, by):
        ans[i][j] = c
        n += 1
        if n >= a[c]:
            c += 1
            n = 0

for i in range(H):
    print(*ans[i])
