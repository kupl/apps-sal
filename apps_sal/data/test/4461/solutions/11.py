
h, w = map(int, input().split())
ans = h * w

if h % 3 == 0 or w % 3 == 0:
    ans = 0
else:
    ans = min(h, w)

a = round(h / 3) * w
b = (h - round(h / 3)) * (w // 2)
c = h * w - a - b
d = max(a, b, c) - min(a, b, c)
ans = min(ans, d)
a = round(w / 3) * h
b = (w - round(w / 3)) * (h // 2)
c = h * w - a - b
d = max(a, b, c) - min(a, b, c)
ans = min(ans, d)
print(ans)
