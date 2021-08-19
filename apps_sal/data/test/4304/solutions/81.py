(a, b) = list(map(int, input().split()))
x = 0
for i in range(1000):
    x += i
    y = x - i
    if a - y == b - x:
        print(y - a)
