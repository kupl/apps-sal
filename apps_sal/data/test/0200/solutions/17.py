(h1, h2) = list(map(int, input().split(' ')))
(a, b) = list(map(int, input().split(' ')))
if h1 + 8 * a >= h2:
    print(0)
elif a <= b:
    print(-1)
else:
    dis = h2 - h1 - 8 * a
    inc = (a - b) * 12
    print((dis + inc - 1) // inc)
