n = int(input())
(b, r, p) = (None, None, None)
ans = 0
mr = -1
mb = -1
for i in range(n):
    (ix, t) = input().split()
    ix = int(ix)
    if t != 'R':
        if b is not None:
            ans += ix - b
            mb = max(mb, ix - b)
        b = ix
    if t != 'B':
        if r is not None:
            ans += ix - r
            mr = max(mr, ix - r)
        r = ix
    if t == 'P':
        if p is not None:
            if ix - p < mr + mb:
                ans -= mr + mb - (ix - p)
        p = ix
        mr = mb = 0
print(ans)
