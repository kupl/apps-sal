H, W, M = map(int, input().split())

Hc = [0 for i in range(H)]
Wc = [0 for i in range(W)]
B = []

for m in range(M):
    h, w = map(int, input().split())
    Hc[h - 1] += 1
    Wc[w - 1] += 1
    B.append((h - 1, w - 1))
Hcmax = max(Hc)
Hcmax_idx = [i for i, x in enumerate(Hc) if x == Hcmax]
Wcmax = max(Wc)
Wcmax_idx = [i for i, x in enumerate(Wc) if x == Wcmax]

ans = Hcmax + Wcmax - 1
B = set(B)
f = False
for i in Hcmax_idx:
    if f:
        break
    for j in Wcmax_idx:
        if (i, j) not in B:
            ans = Hcmax + Wcmax
            f = True
            break
print(ans)
