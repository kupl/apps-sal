def f():
    return int(input())


N = f()
D = [0] * 5
for i in range(5):
    D[i] = f()
m = min(D)
g = -(-(N - m) // m)
print(5 + g)
