def sol(tiles):
    d = {'1': 0, '2': 0}
    for c in tiles:
        if c == ' ':
            continue
        d[c] += 1
    if d['1'] == 0:
        return ' '.join(['2'] * d['2'])
    if d['2'] == 0:
        return ' '.join(['1'] * d['1'])
    return ' '.join(['2','1'] + ['2']*(d['2']-1) + ['1']*(d['1']-1))

def __starting_point():
    _ = input()
    tiles = input()
    print(sol(tiles))

__starting_point()
