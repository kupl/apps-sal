(R, D, x2000) = map(int, input().split())
prev = x2000
for i in range(10):
    x = prev * R - D
    print(x)
    prev = x
