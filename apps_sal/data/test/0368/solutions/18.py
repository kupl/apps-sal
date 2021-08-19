ws = dict(list(zip('qrbnp', (9, 5, 3, 3, 1))))
white = black = 0
for ch in [ch for ch in str.join('', [input() for _ in range(8)]) if ch.lower() not in '.k']:
    if str.isupper(ch):
        white += ws[ch.lower()]
    else:
        black += ws[ch]
if black > white:
    print('Black')
elif black < white:
    print('White')
else:
    print('Draw')
