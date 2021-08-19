(w, h, k) = map(int, input().split())
res = 0
for i in range(k):
    res += (w - 4 * i + h - 4 * i) * 2 - 4
print(res)
