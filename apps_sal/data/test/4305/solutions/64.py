(h, a) = map(int, input().split())
for i in range(10 ** 4 + 1):
    if h - a * i <= 0:
        print(i)
        break
