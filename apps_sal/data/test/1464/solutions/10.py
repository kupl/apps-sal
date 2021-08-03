I = input
s = ' '.join(I()for _ in '0' * int(I()))
R = list(map(chr, range(122, 96, -1)))
for i in R:
    for j in R:
        if s.count(i + j) == 0:
            r = i + j
for i in R:
    if s.count(i) == 0:
        r = i
print(r)
