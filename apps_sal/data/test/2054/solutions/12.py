tests = int(input())
for _ in range(tests):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        print(0)
        continue
    if 2 * x <= y:
        print(x)
    elif 2 * y <= x:
        print(y)
    else:
        print((x + y) // 3)
