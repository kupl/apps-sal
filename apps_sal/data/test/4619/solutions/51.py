import numpy as np
W, H, N = list(map(int, input().split()))
X = [[0 for _ in range(W)] for _ in range(H)]
for i in range(N):
    x, y, a = list(map(int, input().split()))
    if a == 1:  # より左黒
        for j in range(H):
            X[j][:x] = [1 for _ in range(x)]
    elif a == 2:
        for j in range(H):
            X[j][x:] = [1 for _ in range(W - x)]
    elif a == 3:  # より下黒
        for j in range(H - y, H):
            X[j] = [1 for _ in range(W)]
    else:
        for j in range(H - y):
            X[j] = [1 for _ in range(W)]
ans = 0
for k in X:
    ans += k.count(0)
print(ans)
