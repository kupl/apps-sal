H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

c = [[0 for i in range(W)] for i in range(H)]
k = 0
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            c[i][j] = k + 1
            a[k] -= 1
            if a[k] == 0:
                k += 1
    else:
        for j in range(W - 1, -1, -1):
            c[i][j] = k + 1
            a[k] -= 1
            if a[k] == 0:
                k += 1
for i in range(H):
    for j in range(W):
        print(c[i][j], end=' ')
    print()
