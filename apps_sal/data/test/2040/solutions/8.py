(digs, a, le) = ([0] * 333, 0, 0)
for _ in range(int(input())):
    b = int(input())
    (delta, a) = (b - a, b)
    for (i, d) in enumerate(digs):
        if d < 9 and 0 < delta <= 9 * i + 9 - d:
            break
        delta += d
        digs[i] = 0
    digs[i] += 1
    le = max(le, i)
    (i, delta) = divmod(delta - 1, 9)
    digs[:i] = [9] * i
    digs[i] += delta
    print(''.join(map(str, digs[le::-1])))
