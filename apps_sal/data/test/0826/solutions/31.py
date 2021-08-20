N = int(input())
hi = 10 ** 18
lo = -1
while hi - lo > 1:
    md = (hi + lo) // 2
    if md * (md + 1) // 2 <= N + 1:
        lo = md
    else:
        hi = md
print(N + 1 - lo)
