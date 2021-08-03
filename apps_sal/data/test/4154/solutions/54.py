l, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

ll, rr = 1, l
for l, r in lr:
    if ll <= l <= rr or l <= ll <= r:
        ll, rr = max(ll, l), min(rr, r)
    else:
        print(0)
        return
print(rr - ll + 1)
