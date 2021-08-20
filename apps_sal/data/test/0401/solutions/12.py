(m, n) = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a & b
if len(c) != 0:
    print(min(c))
else:
    x = min(a)
    y = min(b)
    if x < y:
        print(x, y, sep='')
    else:
        print(y, x, sep='')
