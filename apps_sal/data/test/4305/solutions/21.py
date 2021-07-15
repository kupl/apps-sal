h,a = list(map(int,input().split()))

b = 0
for i in range(10000000):
    if h > 0:
        h = h - a
        b = b + 1

    else:
        print(b)
        break


