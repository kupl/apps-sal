(w, h, k) = map(int, input().split())
gold = 0
for i in range(k):
    gold += w * h - (w - 2) * (h - 2)
    w -= 4
    h -= 4
print(gold)
