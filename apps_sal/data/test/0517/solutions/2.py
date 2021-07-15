n, w, h = map(int, input().split())
if 2*h < w:
    print(-1)
elif h == w == 1 and n > 2:
    print(-1)
elif h == w == (n - 1):
    last = 1
    for i in range(n - 1):
        print(last, last + 1)
        last += 1
elif h == w:
    last = 0
    for i in range(h):
        last += 1
        print(last, last + 1)
    next = last + 2
    for i in range(n - h - 1):
        print(last, next)
        next += 1
else:
    last = 1
    for i in range(h):
        print(last, last + 1)
        last += 1
    next_l = last + 1
    print(1, next_l)
    next_l += 1
    for i in range(w - h - 1):
        print(next_l, next_l - 1)
        next_l += 1
    n -= (w + 1)
    for i in range(n):
        print(1, next_l)
        next_l += 1
