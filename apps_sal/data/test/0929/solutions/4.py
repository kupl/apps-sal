H, W = map(int, input().split())
A = [list(map(int, input().split())) for h in range(H)]
x = 1
w = 0
ans = []
for h in range(H):
    while 0 <= w + x < W:
        if A[h][w] % 2 == 1:
            ans.append([h + 1, w + 1, h + 1, w + x + 1])
            A[h][w + x] += 1
        w += x
    if A[h][w] % 2 == 1 and h + 1 < H:
        ans.append([h + 1, w + 1, h + 1 + 1, w + 1])
        A[h + 1][w] += 1
    x *= -1
print(len(ans))
for _ in ans:
    print(*_)
