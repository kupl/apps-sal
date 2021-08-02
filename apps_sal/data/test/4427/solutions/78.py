r, d, x = [int(num) for num in input().split(" ")]
for i in range(10):
    x = r * x - d
    print(x)
