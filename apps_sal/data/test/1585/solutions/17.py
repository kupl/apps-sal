(x, y) = map(int, input().split())
for i in range(10 ** 10):
    if x * 2 ** i > y:
        print(i)
        break
