m, R = [int(x) for x in input().split()]

if m == 1:
    print(2 * R)
else:
    tot = 0
    for i in range(m):
        tot += 2
        if i == 0 or i == m - 1:
            tot += 2 + 2**.5
            tot += (m - 2) * (m - 1)
            tot += 2 * 2**.5 * (m - 2)
        else:
            tot += 4 + 2 * 2**.5
            tot += i * (i - 1)
            tot += (m - i - 1) * (m - i - 2)
            tot += 2 * 2**.5 * (m - 3)
    tot *= R
    tot /= m * m
    print(tot)
