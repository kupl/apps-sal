N, = list(map(int, input().split()))
A = list(map(int, input().split()))
s = 0
r = 0
for i, a in enumerate(A):
    s += a
    if i % 2:
        if s >= 0:
            r += s+1
            s = -1
    else:
        if s <= 0:
            r += -s+1
            s = 1
s = 0
r2 = 0
for i, a in enumerate(A):
    s += a
    if i % 2:
        if s <= 0:
            r2 += -s+1
            s = 1
    else:
        if s >= 0:
            r2 += s+1
            s = -1
print((min(r, r2)))

