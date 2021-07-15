x, n = map(int, input().split())
p = sorted(list(map(int, input().split())))
if x not in p:
    print(x)
else:
    for i in range(1, 100):
        x_p, x_m = x + i, x - i
        if x_m not in p:
            print(x_m)
            return
        if x_p not in p:
            print(x_p)
            return
