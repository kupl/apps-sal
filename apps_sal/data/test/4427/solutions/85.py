d = input().split()
r = int(d[0])
D = int(d[1])
x = int(d[2])
for i in range(10):
    x = x * r - D
    print(x)
