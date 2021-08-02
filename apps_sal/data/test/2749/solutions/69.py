with open(0) as f:
    H, W, N, *a = map(int, f.read().split())

line = []
for i in range(N):
    line += [i + 1] * a[i]
ans = [line[i * W:(i + 1) * W] for i in range(H)]
for i, v in enumerate(ans):
    if i & 1:
        v.reverse()
    print(*v)
