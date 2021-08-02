a = []
heights = []
wid = 0
hei = 0
heim = 1000
n = int(input())
for i in range(n):
    w, h = list(map(int, input().split()))
    if (w > h):
        x = w
        w = h
        h = x
    wid += w
    if (hei < h):
        hei = h
    if (heim > w):
        heim = w
    a.append((h, w))
last = wid * hei
for i in range(heim, hei + 1):
    wid1 = 0
    hei1 = i
    for j in range(0, n):
        if a[j][0] <= i:
            wid1 += a[j][1]
        else:
            if (a[j][1] <= i):
                wid1 += a[j][0]
            else:
                wid1 += 1000000000
                break
    if (wid1 * i < last):
        last = wid1 * i
print(last)
