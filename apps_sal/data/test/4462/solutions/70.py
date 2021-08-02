input(); a, b, c, d, r = list(map(int, input().split())), 0, 0, 0, 'NYoe s'
for i in a:
    if i % 2 != 0: b += 1
    elif i % 4 == 0: c += 1
    else: d += 1
print([r[b <= c::2], r[b <= c + 1::2]][not d])
