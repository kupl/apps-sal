h, w = list(map(int, input().split()))

inf = float('inf')

ans = inf

for i in range(1, h):
    a = i * w
    rest = h * w - a
    b = (w // 2) * (h - i)
    c = rest - b
    max_s = max(a, b, c)
    min_s = min(a, b, c)
    ans = min(ans, max_s - min_s)

for j in range(1, w):
    A = j * h
    Rest = h * w - A
    B = (h // 2) * (w - j)
    C = Rest - B
    Max_s = max(A, B, C)
    Min_s = min(A, B, C)
    ans = min(ans, Max_s - Min_s)

if w >= 3:
    if w % 3 == 0:
        ans = 0
    else:
        ans = min(ans, h)

if h >= 3:
    if h % 3 == 0:
        ans = 0
    else:
        ans = min(ans, w)

print(ans)
