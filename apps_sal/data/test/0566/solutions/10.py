balloons = list(map(int, input().split(' ')))
balloons.sort()
a, b, c = list(map(int, balloons))
if a + b <= int(c / 2):
    print(a + b)
else:
    print((a + b + c) // 3)
