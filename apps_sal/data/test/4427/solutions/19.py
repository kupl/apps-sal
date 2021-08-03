r, D, x2000 = map(int, input().split())
n = x2000
for i in range(10):
    x = r * n - D
    print(x)
    n = x
