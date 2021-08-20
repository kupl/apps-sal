import math
(c, hr, hb, wr, wb) = map(int, input().split())
s = int(math.sqrt(c))
ans = 0
for i in range(s):
    if c >= i * wr:
        ans = max(ans, hr * i + (c - i * wr) // wb * hb)
    if c >= i * wb:
        ans = max(ans, hb * i + (c - i * wb) // wr * hr)
print(ans)
