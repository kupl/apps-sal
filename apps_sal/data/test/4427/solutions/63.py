r, d, x = map(int, input().split())
output = r * x - d
for i in range(10):
    print(output)
    output = output * r - d
