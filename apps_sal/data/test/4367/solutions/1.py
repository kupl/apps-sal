n, x = list(map(int, input().split()))
if n >= 10:
    print(x)
else:
    y = x + (10 - n) * 100
    print(y)
