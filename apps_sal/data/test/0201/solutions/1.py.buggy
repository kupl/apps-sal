m, h1, h2, w1, w2 = map(int, input().split())
if h2 / w2 > h1 / w1:
    h1, h2 = h2, h1
    w1, w2 = w2, w1
if w1 ** 2 >= m:
    res = 0
    for i in range(int(m ** 0.5 + 1)):
        if i * w1 <= m:
            new = i * h1 + (m - w1 * i) // w2 * h2
            res = max(res, new)
    print(res)
    return
res = 0
for i in range(int(m ** 0.5 + 5)):
    new_res = i * h2 + ((m - i * w2) // w1) * h1
    res = max(res, new_res)
print(res)
