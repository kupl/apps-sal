(w, h) = map(int, input().split())
(u1, d1) = map(int, input().split())
(u2, d2) = map(int, input().split())
for i in range(h, 0, -1):
    w += i
    if i == d1:
        w -= u1
        if w < 0:
            w = 0
    elif i == d2:
        w -= u2
        if w < 0:
            w = 0
print(w)
