(W, H, N) = map(int, input().split())
(a1, a2, a3, a4) = (-1, 101, -1, 101)
for i in range(N):
    (x, y, a) = map(int, input().split())
    if a == 1:
        a1 = max(a1, x)
    elif a == 2:
        a2 = min(a2, x - 1)
    elif a == 3:
        a3 = max(a3, y)
    else:
        a4 = min(a4, y - 1)
mass = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i < a3 or a4 < i:
            mass[i][j] += 1
        if j < a1 or a2 < j:
            mass[i][j] += 1
cnt = 0
for k in mass:
    cnt += k.count(0)
print(cnt)
