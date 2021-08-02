w, h, k = list(map(int, input().split()))
s = 0
for i in range(k):
    s += 2 * (w - 2 - 4 * i) + 2 * (h - 2 - 4 * i) + 4
print(s)
