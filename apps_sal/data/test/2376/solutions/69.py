N, W, *WV = map(int, open(0).read().split())

C = {0: 0}
for v, w in zip(*[reversed(WV)] * 2):
    for x, y in C.copy().items():
        if x + w <= W:
            C[x + w] = max(C.get(x + w, 0), y + v)

print(max(C.values()))
