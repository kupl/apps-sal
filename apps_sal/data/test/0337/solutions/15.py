(w, h) = list(map(int, input().split(' ')))
(u1, d1) = list(map(int, input().split(' ')))
(u2, d2) = list(map(int, input().split(' ')))
while h > 0:
    w += h
    if d1 == h:
        w -= u1
    w = max(w, 0)
    if d2 == h:
        w -= u2
    w = max(w, 0)
    h -= 1
print(max(w, 0))
