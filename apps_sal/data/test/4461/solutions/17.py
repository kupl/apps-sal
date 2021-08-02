h, w = map(int, input().split())
mini = h * w
for i in range(1, h):
    if mini > max(w * (h - i), (w // 2 + w % 2) * i) - min(w * (h - i), (w // 2) * i):
        mini = max(w * (h - i), (w // 2 + w % 2) * i) - min(w * (h - i), (w // 2) * i)

for i in range(1, w):
    if mini > max(h * (w - i), (h // 2 + h % 2) * i) - min(h * (w - i), (h // 2) * i):
        mini = max(h * (w - i), (h // 2 + h % 2) * i) - min(h * (w - i), (h // 2) * i)

if h % 3 == 0 or w % 3 == 0:
    mini = 0
else:
    if mini > h:
        mini = h
    elif mini > w:
        mini = w
    else:
        pass
print(mini)
