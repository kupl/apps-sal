m, c2, c5, i, v = int(input()), 0, 0, 1, []
while min(c2, c5) <= m:
    c = i
    while c % 2 == 0:
        c, c2 = c // 2, c2 + 1
    while c % 5 == 0:
        c, c5 = c // 5, c5 + 1
    if min(c2, c5) == m:
        v.append(i)
    i += 1
print(len(v))
if v:
    print(' '.join(map(str, v)))
