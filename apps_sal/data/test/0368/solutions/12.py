m = []

f = {
    '.': 0,
    'q': -9,
    'r': -5,
    'b': -3,
    'n': -3,
    'p': -1,
    'k': 0,
    'Q': 9,
    'R': 5,
    'B': 3,
    'N': 3,
    'P': 1,
    'K': 0,
}

for i in range(8):
    m.append(list(input()))

cnt = 0

for s in m:
    for c in s:
        if c in f:
            cnt += f[c]


if cnt > 0:
    print('White')
elif cnt < 0:
    print('Black')
else:
    print('Draw')
