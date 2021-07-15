H, W, M = list(map(int, input().split()))
bombs = set([tuple(map(int, input().split())) for _ in range(M)])

cntH = [0] * (H + 1)
cntW = [0] * (W + 1)
for h, w in bombs:
    cntH[h] += 1
    cntW[w] += 1

mxH = max(cntH)
mxW = max(cntW)

ans = mxH + mxW - 1

mxH = [h for h in range(1, H + 1) if cntH[h] == mxH]
mxW = [w for w in range(1, W + 1) if cntW[w] == mxW]

for h in mxH:
    for w in mxW:
        if not (h, w) in bombs:
            ans += 1
            print(ans)
            return
print(ans)

