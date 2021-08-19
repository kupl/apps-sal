cal = {i: j for (i, j) in zip('monday tuesday wednesday thursday friday saturday sunday'.split(), range(7))}
fst = cal[input()]
snd = cal[input()]
gre = {0, 2, 3}
print('YES' if (snd - fst) % 7 in gre else 'NO')
