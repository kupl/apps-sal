(w, h) = list(map(int, input().split()))
(u1, d1) = list(map(int, input().split()))
(u2, d2) = list(map(int, input().split()))
for i in range(h, -1, -1):
    w += i
    if i == d1:
        w -= u1
    if i == d2:
        w -= u2
    w = max(w, 0)
print(w)
