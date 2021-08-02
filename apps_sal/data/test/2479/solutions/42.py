N, Q = map(int, input().split())
a, b = [N] * (N + 1), [N] * (N + 1)

H, W = N, N

black = (N - 2)**2

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        if x < W:
            for i in range(x, W):
                b[i] = H
            W = x

        black -= b[x] - 2

    else:
        if x < H:
            for i in range(x, H):
                a[i] = W
            H = x

        black -= a[x] - 2


print(black)
