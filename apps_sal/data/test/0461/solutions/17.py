n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n == 1:
    print(0)
else:
    mi = min(a, b, c)
    if mi == a:
        dist = a * (n - 1)
    elif mi == b:
        dist = b * (n - 1)
    elif mi == c:
        ma = min(a, b)
        if ma == a:
            dist = a
        else:
            dist = b
        dist = dist + c * (n - 2)
    print(dist)
