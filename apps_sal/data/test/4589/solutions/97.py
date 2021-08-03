H, W = map(int, input().split())
L = []
for i in range(H):
    S = list(input())
    L.append(S)

for i in range(H):
    for j in range(len(L[i])):
        if L[i][j] == '.':
            cnt = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if ((i + k) < H) and ((j + l) < len(L[i])) and ((j + l) >= 0) and ((i + k) >= 0):
                        if L[i + k][j + l] == '#':
                            cnt += 1
            L[i][j] = str(cnt)

for i in range(len(L)):
    print(''.join(L[i]))
