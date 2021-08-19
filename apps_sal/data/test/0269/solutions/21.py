s = input()
col_idx = {}
counts = [0, 0, 0, 0]
for (i, c) in enumerate(s):
    if c == '!':
        counts[i % 4] += 1
    else:
        col_idx[c] = i % 4
print('%d %d %d %d' % tuple((counts[col_idx[c]] for c in 'RBYG')))
