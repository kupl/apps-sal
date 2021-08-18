import bisect
n = int(input())
a = list(map(int, input().split()))

cum = [0]
for ai in a:
    cum.append(cum[-1] + ai)

ans = float('inf')

for i in range(2, n - 1):
    bc = cum[i]
    de = cum[-1] - cum[i]
    bc_mid = bc / 2
    de_mid = (cum[i] + cum[-1]) / 2

    i_bc = bisect.bisect_left(cum, bc_mid)
    i_de = bisect.bisect_left(cum, de_mid)

    for cum_b in (cum[i_bc - 1], cum[i_bc]):
        for cum_d in (cum[i_de - 1], cum[i_de]):
            b = cum_b
            c = bc - b
            d = cum_d - bc
            e = de - d
            bcde = [b, c, d, e]
            bcde.sort()
            ans = min(ans, bcde[-1] - bcde[0])

print(ans)
