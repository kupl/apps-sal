(n, d) = list(map(int, input().split()))
X = []
for i in range(n):
    a = list(map(int, input().split()))
    X.append(a)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        norm = 0
        for k in range(d):
            diff = abs(X[i][k] - X[j][k])
            norm += diff * diff
        can = False
        for k in range(1, norm + 1):
            if k * k == norm:
                can = True
        if can:
            count += 1
print(count)
