def __starting_point():
    inp = input()
    inp = input()
    L = []
    for iv in inp.split(' '):
        L.append(int(iv))
    vals = [0, 0, 0]
    ans = 'YES'
    for iv in L:
        if iv == 25:
            vals[0] += 1
        if iv == 50:
            if vals[0] > 0:
                vals[0] -= 1
                vals[1] += 1
            else:
                ans = 'NO'
                break
        if iv == 100:
            if vals[0] > 0 and vals[1] > 0:
                vals[2] += 1
                vals[0] -= 1
                vals[1] -= 1
            elif vals[0] > 2:
                vals[0] -= 3
                vals[2] += 1
            else:
                ans = 'NO'
                break
    print(ans)


__starting_point()
