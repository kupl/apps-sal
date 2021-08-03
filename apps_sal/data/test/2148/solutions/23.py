import math
n, r = map(int, input().split())
X = list(map(int, input().split()))
C = []
for q in range(len(X)):
    y = r
    for w in range(len(C)):
        if abs(X[w] - X[q]) <= 2 * r:
            yc = math.sqrt(4 * r * r - (X[w] - X[q]) ** 2) + C[w]
            # print(yc);
            y = max(y, yc)
    C.append(y)
print(*C)
