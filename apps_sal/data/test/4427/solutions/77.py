r, D, x = map(int, input().split())

X = []
X.append(x)

for i in range(10):
    x = r * X[i] - D
    X.append(x)
    print(x)
