(H, W) = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
C = [[] for i in range(H)]
for (i, (arow, brow)) in enumerate(zip(A, B)):
    for (a, b) in zip(arow, brow):
        d = abs(a - b)
        C[i].append(d)
ofs = (H + W) * 100
dp = [0] * W
dp[0] = 1 << ofs
for (i, crow) in enumerate(C):
    dp2 = [0] * W
    for (j, (c, d)) in enumerate(zip(C[i], dp)):
        dp2[j] |= d << c
        dp2[j] |= d >> c
    for (j, c) in enumerate(C[i]):
        if j == 0:
            continue
        dp2[j] |= dp2[j - 1] << c
        dp2[j] |= dp2[j - 1] >> c
    dp = dp2
ans = ofs
l = len(bin(dp[-1]))
for i in range(l):
    if dp[-1] & 1 << i:
        ans = min(ans, abs(i - ofs))
print(ans)
