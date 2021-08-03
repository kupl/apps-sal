t = int(input())
for i in range(t):
    c0, c1 = map(int, input().split())
    ma, mb = map(int, input().split())
    wa, wb = map(int, input().split())

    ans = 0
    if wa > wb:
        wa, wb = wb, wa
        ma, mb = mb, ma
    for i in range(ma + 1):
        c0a = min(i, c0 // wa)
        c1a = min(ma - i, c1 // wa)
        n0 = c0 - c0a * wa
        n1 = c1 - c1a * wa
        ans0 = c0a + c1a
        c01b = min(mb, n0 // wb + n1 // wb)
        ans0 += c01b
        ans = max(ans, ans0)
    print(ans)
