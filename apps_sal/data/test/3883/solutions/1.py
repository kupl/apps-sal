a, b = list(map(int, input().split()))
if b > a:
    print(-1)
else:
    try:
        x = 100000000000
        k = int((a + b) / 2 / b)
        if k != 0:
            x = (a + b) / 2 / k
        k = int((a - b) / 2 / b)
        if k != 0:
            x = min(x, (a - b) / 2 / k)
        print("%.9f" % x)
    except:
        print(-1)
