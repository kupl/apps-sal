figures = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1, 'k': 0}
(black_w, white_w) = (0, 0)
for _ in range(0, 8):
    row = input().strip()
    for c in row:
        if c.lower() in figures:
            if c.lower() == c:
                black_w += figures[c]
            else:
                white_w += figures[c.lower()]
if black_w == white_w:
    print('Draw')
elif black_w > white_w:
    print('Black')
else:
    print('White')
