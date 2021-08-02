p = {'K': 0, 'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1, '.': 0}
w = [0, 0]
for r in range(8):
    for ch in input():
        if ch != '.':
            w[ch.islower()] += p[ch.upper()]
if w[0] == w[1]:
    print('Draw')
else:
    print('White' if w[0] > w[1] else 'Black')
