(r, D, x2000) = map(int, input().split())
for i in range(10):
    x = r * x2000 - D
    print(x)
    x2000 = x
