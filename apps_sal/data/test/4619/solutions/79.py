W, H, N = map(int, input().split())
x = []
y = []
a = []
X = [1]*W
Y = [1]*H
ans = 0
for _ in range(N):
    i, j, k = map(int, input().split())
    x.append(i)
    y.append(j)
    a.append(k)
for i in range(N):
    if a[i] == 1:
        for j in range(x[i]):
            X[j] = 0
    elif a[i] == 2:
        for j in range(x[i], W):
            X[j] = 0
    elif a[i] == 3:
        for j in range(y[i]):
            Y[j] = 0
    else:
        for j in range(y[i], H):
            Y[j] = 0
for i in range(H):
    for j in range(W):
        if X[j] and Y[i]:
            ans += 1
print(ans)
