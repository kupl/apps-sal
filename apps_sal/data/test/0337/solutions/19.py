w, h = list(map(int, input().split()))
u1, d1 = list(map(int, input().split()))
u2, d2 = list(map(int, input().split()))
for i in range(h, 0, -1):
    w += i
    if i == d1:
        w = max(0, w - u1)
    if i == d2:
        w = max(0, w - u2)
print(w)
