N, *A = list(map(int, open(0).read().split()))
mx, mn = 0, 1_000_000_000
for a in A:
    mx = max(mx, a)
    mn = min(mn, a)
print((mx - mn))
