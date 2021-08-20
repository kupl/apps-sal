(r, n) = [int(x) for x in input().split()]
cells = [[int(x) for x in input().split()] for i in range(n)]
cells.sort()
out = False
res = {True: 'WIN', False: 'LOSE'}
if len(cells) == 0:
    print(res[r % 2 == 1])
else:
    out = False
    for i in range(1, n):
        out ^= (cells[i][0] - cells[i - 1][0] - 1) % 2 ^ (cells[i][1] != cells[i - 1][1])
    dif = abs(cells[0][0] - 1 - (r - cells[-1][0]))
    (hi, lo) = (max(cells[0][0] - 1, r - cells[-1][0]), min(cells[0][0] - 1, r - cells[-1][0]))
    if lo > 1:
        if dif == 0:
            print(res[out])
        elif dif == 1 and lo % 2 == 0:
            print(res[not out])
        else:
            print(res[True])
    elif lo == 0:
        if hi == 0:
            print(res[out])
        elif hi == 1:
            print(res[not out])
        else:
            print(res[True])
    elif lo == 1:
        if hi == 1:
            print(res[out])
        else:
            print(res[True])
