H, W = map(int, input().split())

dif = 10**10

if H % 3 == 0 or W % 3 == 0:
    print(0)
    return

for i in range(H):
    a = i * W
    h = (H - i) // 2
    abc = [a, h * W, (H - i - h) * W]
    if not(0 in abc):
        dif = min(dif, max(abc) - min(abc))

    h = H - i
    w = W // 2
    abc = [a, h * w, h * (W - w)]
    if not(0 in abc):
        dif = min(dif, max(abc) - min(abc))

for i in range(W):
    a = H * i
    w = (W - i) // 2
    abc = [a, H * w, H * (W - i - w)]
    if not(0 in abc):
        dif = min(dif, max(abc) - min(abc))

    w = W - i
    h = H // 2
    abc = [a, h * w, (H - h) * w]
    if not(0 in abc):
        dif = min(dif, max(abc) - min(abc))

print(dif)
