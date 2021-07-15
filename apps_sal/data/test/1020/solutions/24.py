w, h, k = map(int, input().split())
r = 0
for i in range(k):
    r += w * 2
    r += (h - 2) * 2
    w -= 4
    h -= 4
print(r)
