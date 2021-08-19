H, W, K = map(int, input().split())
c = [tuple(input()) for i in range(H)]
ans = 0
for i in range(2**H):
    s = i
    b = [list(x) for x in c]
    for j in range(H):
        if s >= (2**(H - j - 1)):
            s -= 2**(H - j - 1)
            b[j] = ["."] * W
    b = list(zip(*b))
    for k in range(2**W):
        bt = [list(x) for x in b]
        t = k
        for l in range(W):
            if t >= (2**(W - l - 1)):
                t -= 2**(W - l - 1)
                bt[l] = ["."] * H
        u = sum(bt[m].count("#") for m in range(W))
        if u == K:
            ans += 1
print(ans)
