t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    if 2 * a >= b:
        print(min(x, y) * b + (x + y - 2 * min(x, y)) * a)
    else:
        print((x + y) * a)

