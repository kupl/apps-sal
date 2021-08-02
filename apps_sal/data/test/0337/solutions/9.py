w, h = list(map(int, input().split()))
u1, d1 = list(map(int, input().split()))
u2, d2 = list(map(int, input().split()))
for H in range(h, -1, -1):
    w += H
    if H == d1:
        w = max(0, w - u1)
    if H == d2:
        w = max(0, w - u2)
print(w)
