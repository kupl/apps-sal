(n, r) = list(map(int, input().split()))
X = [int(x) for x in input().split()]
Y = []
for i in range(n):
    forcedy = r
    for j in range(len(Y)):
        dist = abs(X[i] - X[j])
        if dist <= 2 * r:
            y = Y[j] + ((2 * r) ** 2 - dist ** 2) ** 0.5
            forcedy = max(y, forcedy)
    Y.append(forcedy)
print(*Y)
