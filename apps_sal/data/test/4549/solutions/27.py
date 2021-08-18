H, W = map(int, input().split())
L = ['.' + input() + '.' for _ in range(H)]
L = ['.' * (W + 2)] + L + ['.' * (W + 2)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if L[i][j] == "
        l = [L[i - 1][j], L[i + 1][j], L[i][j - 1], L[i][j + 1]]
        if '
        print('No')
        break
    else:
        continue
    break
else:
    print('Yes')
