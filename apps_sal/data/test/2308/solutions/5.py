t = int(input())
for _ in range(t):
    x = input()
    y = input()
    r = y.rfind('1')
    if r < 0:
        print(0)
    else:
        l = len(x) - len(y) + r
        print(l - x[:l + 1].rfind('1'))
