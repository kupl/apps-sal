n = int(input())
xm = ym = -10000000
for _ in range(n):
    xi, yi = list(map(int, input().split()))
    xm, ym = max((xi, yi), (xm, ym))
am = bm = 10000000
for _2 in range(n):
    ai, bi = list(map(int, input().split()))
    am, bm = min((ai, bi), (am, bm))
print(am + xm, bm + ym)

