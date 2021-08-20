(r, D, x2000) = map(int, input().split())
x = r * x2000 - D
for i in range(1, 10 + 1):
    print(x)
    x = r * x - D
