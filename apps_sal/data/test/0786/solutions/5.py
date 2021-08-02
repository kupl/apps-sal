n = int(input())
INF = 2 ** 60
lo, hi = -INF, INF
for i in range(n):
    x, y = (int(_) for _ in input().split())
    if y == 2:
        hi = min(hi, 1899)
    else:
        lo = max(lo, 1900)
    hi += x
    lo += x
if lo > hi:
    print('Impossible')
elif hi > 2 ** 31:
    print('Infinity')
else:
    print(hi)
