h = int(input())
l = [c == '#' for _ in range(h) for c in input()]
w = len(l) // h
pattern = (0, w - 1, w, w + 1, 2 * w)
for idx in range(1, (h - 2) * w - 1):
    if all(l[_ + idx] for _ in pattern):
        for _ in pattern:
            l[_ + idx] = False
print(('YES', 'NO')[any(l)])
