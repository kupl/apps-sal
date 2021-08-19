(H, W, D) = list(map(int, input().split()))
(d, px, py) = ([0] * (H * W + 1), [0] * (H * W + 1), [0] * (H * W + 1))
for i in range(H):
    a = list(map(int, input().split()))
    for j in range(W):
        px[a[j]] = i
        py[a[j]] = j
for i in range(D + 1, H * W + 1):
    d[i] = d[i - D] + abs(px[i] - px[i - D]) + abs(py[i] - py[i - D])
Q = int(input())
for _ in range(Q):
    (l, r) = list(map(int, input().split()))
    print(d[r] - d[l])
