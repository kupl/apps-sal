H, W, D = list(map(int, input().split()))

base = []
for h in range(H):
    num = list(map(int, input().split()))
    for w in range(W):
        base.append((num[w], h + 1, w + 1))

base.sort(key=lambda tup: tup[0])
dist = [0] * (W * H + D + 1)
for i in range(W * H - D):
    wei1, h1, w1 = base[i]
    wei2, h2, w2 = base[i + D]
    dist[i + D] = dist[i] + abs(h1 - h2) + abs(w1 - w2)

Q = int(input())
for _ in range(Q):
    p0, p1 = list(map(int, input().split()))
    print((abs(dist[p1 - 1] - dist[p0 - 1])))
