(h, w) = map(int, input().split())
stand = h * w / 3
(prevh, prevw) = (1, 1)
mini = 10 ** 18
for i in range(2, h + 1):
    if abs(stand - i * w) < abs(stand - prevh * w):
        prevh = i
if h - prevh >= 2:
    mini = min(mini, max((h - prevh) // 2 * w, prevh * w, -(-(h - prevh) // 2) * w) - min((h - prevh) // 2 * w, prevh * w, -(-(h - prevh) // 2) * w))
mini = min(mini, max(w // 2 * (h - prevh), prevh * w, -(-w // 2) * (h - prevh)) - min(w // 2 * (h - prevh), prevh * w, -(-w // 2) * (h - prevh)))
for i in range(2, w + 1):
    if abs(stand - i * h) < abs(stand - prevw * h):
        prevw = i
if w - prevw >= 2:
    mini = min(mini, max((w - prevw) // 2 * h, prevw * h, -(-(w - prevw) // 2) * h) - min((w - prevw) // 2 * h, prevw * h, -(-(w - prevw) // 2) * h))
mini = min(mini, max(h // 2 * (w - prevw), prevw * h, -(-h // 2) * (w - prevw)) - min(h // 2 * (w - prevw), prevw * h, -(-h // 2) * (w - prevw)))
print(mini)
