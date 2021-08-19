(r, d, x) = list(map(int, input().split()))
for i in range(1, 11):
    x = r * x - d
    print(x)
