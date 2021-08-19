(w, h, k) = map(int, input().split())
s = 0
for i in range(k):
    s += 2 * (w - 4 * i) + 2 * (h - 4 * i) - 4
print(s)
