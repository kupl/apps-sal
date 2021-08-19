(H, W) = map(int, input().split())
anslist = [['#' for i in range(W + 2)] for j in range(H + 2)]
for i in range(H):
    a = input()
    for j in range(W):
        anslist[i + 1][j + 1] = a[j]
for i in range(H + 2):
    for j in range(W + 2):
        print(anslist[i][j], end='')
    print()
