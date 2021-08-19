(H, W, D) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
lst = [[] for _ in range(H * W)]
for i in range(H):
    for j in range(W):
        lst[A[i][j] - 1] = [j, i]
tr = [[0] for _ in range(D)]
for i in range(D):
    for j in range(i + D, W * H, D):
        dlt = abs(lst[j][0] - lst[j - D][0]) + abs(lst[j][1] - lst[j - D][1])
        tr[i].append(tr[i][-1] + dlt)
Q = int(input())
for i in range(Q):
    (l, r) = map(int, input().split())
    idx = (l - 1) % D
    if (l - 1) // D == 0:
        st = 0
    else:
        st = (l - 1) // D
    ed = (r - 1) // D
    print(tr[idx][ed] - tr[idx][st])
