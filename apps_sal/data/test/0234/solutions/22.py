para = input().split(' ')
para = [int(e) for e in para]
big = []
for i in range(para[0]):
    small = input().strip()
    assert len(small) == para[1]
    l = []
    for c in small:
        if c == '*':
            l.append(100)
        elif c == '.':
            l.append(0)
        else:
            assert c in '12345678'
            l.append(int(c))
    big.append(l)
for i in range(len(big)):
    for j in range(len(big[0])):
        if big[i][j] > 50:
            for ii in [i - 1, i, i + 1]:
                for jj in [j - 1, j, j + 1]:
                    if ii >= 0 and ii < len(big) and (jj >= 0) and (jj < len(big[0])):
                        big[ii][jj] -= 1
result = True
for i in range(len(big)):
    for j in range(len(big[0])):
        if big[i][j] == 0 or big[i][j] > 50:
            continue
        else:
            result = False
            break
    if not result:
        break
if result:
    print('YES')
else:
    print('NO')
