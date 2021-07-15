K, X = map(int, input().split())

Y = []

for i in range(X - (K - 1), X + K):
    Y.append(str(i))

print(" ".join(Y))
