l, r, x, y = list(map(int, input().split()))
h = ()
a = 0
if y % x < 1:
    y //= x
    s = y
    l = (l - 1) // x + 1
    r //= x
    i = 2
    while i * i <= y:
        j = 1
        while y % i < 1:
            j *= i
            y //= i
        if j > 1:
            h += j,
        i += 1
    if y > 1:
        h += y,
    for i in range(1 << len(h)):
        p = 1
        for j, u in enumerate(h):
            if(i >> j) & 1:
                p *= u
        a += l <= p <= r and l <= s // p <= r
print(a)
