x = []
(r, D, a) = map(int, input().split())
x.append(a)
for i in range(10):
    x.append(r * x[i] - D)
    print(x[i + 1])
