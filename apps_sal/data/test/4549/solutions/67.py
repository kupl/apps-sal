import sys
H, W = map(int, input().split())
lsHW = [['.' for i in range(W + 2)]]
for i in range(H):
    Sls = ['.'] + list(input()) + ['.']
    lsHW.append(Sls)
lsHW.append(['.' for i in range(W + 2)])
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if lsHW[i][j] == '.':
            continue
        else:
            if not (lsHW[i - 1][j] == '#' or lsHW[i + 1][j] == '#' or lsHW[i][j - 1] == '#' or lsHW[i][j + 1] == '#'):
                print('No')
                return
print('Yes')
