(W, H, N) = list(map(int, input().split()))
xs = ys = 0
xe = W
ye = H
for i in range(N):
    (x, y, a) = list(map(int, input().split()))
    if a == 1 and x > xs:
        xs = x
    elif a == 2 and x < xe:
        xe = x
    elif a == 3 and y > ys:
        ys = y
    elif a == 4 and y < ye:
        ye = y
w = xe - xs
h = ye - ys
if w > 0 and h > 0:
    ans = w * h
else:
    ans = 0
print(ans)
