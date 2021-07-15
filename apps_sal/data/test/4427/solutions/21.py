r, d, x = map(int, input().split())

weights = []
for i in range(10):
    if i == 0:
        weights.append(r * x - d)
        print(weights[i])
    else:
        weights.append(r * weights[i - 1] - d)
        print(weights[i])
