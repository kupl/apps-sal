W, H, N = list(map(int, input().split()))
white = [[1 for _ in range(H)] for _ in range(W)]

for i in range(N):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        for i in range(x):
            for j in range(H):
                white[i][j] = 0
    elif a == 2:
        for i in range(x, W):
            for j in range(H):
                white[i][j] = 0
    elif a == 3:
        for i in range(W):
            for j in range(y):
                white[i][j] = 0
    else:
        for i in range(W):
            for j in range(y, H):
                white[i][j] = 0
print((sum(sum(x) for x in white)))
