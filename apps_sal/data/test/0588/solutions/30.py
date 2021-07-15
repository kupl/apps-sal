L = 10**10

N = int(input())
x, y = zip(*(map(int, input().split()) for _ in range(N)))

result = 0
for i in range(N):
    for b in [-1, 1]:
        for s, t in [(y[i], -x[i]), (-y[i], x[i])]:
            s, t = L * s - b * t, b * s + L * t
            X = 0
            Y = 0
            for j in range(N):
                if x[j] * s + y[j] * t > 0:
                    X += x[j]
                    Y += y[j]
            result = max(result, (X**2 + Y**2)**0.5)
print(result)
