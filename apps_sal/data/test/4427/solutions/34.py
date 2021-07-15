r, d, x = map(int, input().split())

weights = []
for i in range(10):
    try:
        weights.append(r * weights[i - 1] - d)
        print(weights[i])
    except:
        weights.append(r * x - d)
        print(weights[i])
