h = int(input())
l = [c == '#' for _ in range(h) for c in input()]
w = len(l) // h
cross = (0, w - 1, w, w + 1, 2 * w)
for i in range(1, (h - 2) * w - 1):
    if all(l[_ + i] for _ in cross):
        for _ in cross:
            l[_ + i] = False
print(('YES', 'NO')[any(l)])

