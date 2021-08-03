n, x, y = map(int, input().split())
a = input() + "1"
cnt = a.count("01")
if cnt == 0:
    print(0)
else:
    print((cnt - 1) * min(x, y) + y)
