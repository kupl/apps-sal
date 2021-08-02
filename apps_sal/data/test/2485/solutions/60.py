def solve(H, W, M, h, w):
    f = [0] * (H + 1)
    g = [0] * (W + 1)
    for r, c in zip(h, w):
        f[r] += 1
        g[c] += 1
    p = max(f)
    q = max(g)
    num = len(list(filter(p.__eq__, f))) * len(list(filter(q.__eq__, g)))
    num -= len(list(filter(lambda _: f[_[0]] + g[_[1]] == p + q, zip(h, w))))
    return p + q - (num <= 0)


H, W, M = map(int, input().split())
h, w = zip(*[map(int, input().split()) for i in range(M)])
print(solve(H, W, M, h, w))
