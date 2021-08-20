(H, W) = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
data = [[] for _ in range(H)]
k = 0
for i in range(N):
    for j in range(a[i]):
        data[k].append(i + 1)
        if len(data[k]) == W:
            k += 1
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            print(data[i][j], '', end='')
    else:
        for j in range(W):
            print(data[i][W - j - 1], '', end='')
    print()
