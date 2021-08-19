n, s = list(map(int, input().split()))
a = []
ind = True
for i in range(n):
    x, y = list(map(int, input().split()))
    time = (60 * x) + y
    if len(a) == 0 and time >= s + 1 and ind:
        print(0, 0)
        ind = False
    elif len(a) > 0 and ind:
        last = a[len(a) - 1]
        if time - last >= (2 * s) + 2:
            y = last + s + 1
            print(y // 60, y % 60)
            ind = False
    a.append(time)
# print(a)
if ind:
    y = a[len(a) - 1] + s + 1
    # print(y)
    print(y // 60, y % 60)
