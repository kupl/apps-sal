(W, H, N) = map(int, input().split())
a = []
for i in range(N):
    b = list(map(int, input().split()))
    a.append(b)
xs = 0
xe = W
ys = 0
ye = H
for i in range(N):
    if a[i][2] == 1 and xs < a[i][0]:
        xs = a[i][0]
    elif a[i][2] == 2 and xe > a[i][0]:
        xe = a[i][0]
    elif a[i][2] == 3 and ys < a[i][1]:
        ys = a[i][1]
    elif a[i][2] == 4 and ye > a[i][1]:
        ye = a[i][1]
if xs < xe:
    w = xe - xs
else:
    w = 0
if ys < ye:
    h = ye - ys
else:
    h = 0
print(w * h)
