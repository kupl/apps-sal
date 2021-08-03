r, D, x = map(int, input().split())
now = x
for i in range(10):
    x = x * r - D
    print(x)
