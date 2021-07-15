n, a, b, c = map(int,input().split())
ost = (-n) % 4
if ost == 0:
    print(0)
elif ost == 1:
    print(min(a, 3 * c, b + c))
elif ost == 2:
    print(min(2 * a, b, 2 * c))
else:
    print(min(3 * a, c, b + a))
