h, w = map(int, input().split())
if (h % 3 == 0) or (w % 3 == 0):
    print(0)
else:
    ans = h * w
    for i in range(1, max(h, w) // 2 + 1):
        a = min(h, w) * i
        b = (max(h, w) - i) * (min(h, w) // 2)
        if min(h, w) % 2 != 0:
            c = (max(h, w) - i) * (min(h, w) // 2 + 1)
        else:
            c = b
        kari = max(a, b, c) - min(a, b, c)
        if ans > kari:
            ans = kari
    ans3 = h * w
    for i in range(1, min(h, w) // 2 + 1):
        a = max(h, w) * i
        b = (min(h, w) - i) * (max(h, w) // 2)
        if max(h, w) % 2 != 0:
            c = (min(h, w) - i) * (max(h, w) // 2 + 1)
        else:
            c = b
        kari = max(a, b, c) - min(a, b, c)
        if ans3 > kari:
            ans3 = kari
    ans2 = ((max(h, w) // 3 + 1) * min(h, w)) - ((max(h, w) // 3) * min(h, w))
    print(min(ans, ans2, ans3))
