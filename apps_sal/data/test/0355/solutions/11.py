white, black = [set() for _ in range(8)], [set() for _ in range(8)]
for row in range(8):
    for col, c in enumerate(input().strip()):
        if c == 'W':
            white[col].add(row)
        elif c == 'B':
            black[col].add(row)

min_w, max_b = 7, 0
for col in range(8):
    for w in white[col]:
        if all(b > w for b in black[col]) and w < min_w:
            min_w = w
    for b in black[col]:
        if all(b > w for w in white[col]) and b > max_b:
            max_b = b

if min_w <= 7 - max_b:
    print('A')
else:
    print('B')
