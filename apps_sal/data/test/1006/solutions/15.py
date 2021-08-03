c = set()
for i in range(int(input())):
    row = input()
    s = [(i, j) for j in range(len(row)) if row[j] == '#']
    c |= set(s)
    for i, j in s:
        p = set([(i, j), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1), (i - 2, j)])
        if p <= c:
            c -= p
print('YNEOS'[len(c) != 0::2])
