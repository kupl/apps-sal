r, d, x = map(int, input().split())
l = []
for i in range(10):
    x = r * x - d
    print(x, "\n")
