(w, h, n) = map(int, input().split())
W = [1] * w
H = [1] * h
for i in range(n):
    (x, y, a) = map(int, input().split())
    if a == 1:
        for j in range(x):
            W[j] = 0
    elif a == 2:
        for j in range(x, w):
            W[j] = 0
    elif a == 3:
        for j in range(y):
            H[j] = 0
    elif a == 4:
        for j in range(y, h):
            H[j] = 0
print(sum(W) * sum(H))
