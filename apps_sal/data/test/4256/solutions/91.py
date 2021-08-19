(a, b, c) = list(map(int, input().split()))
x = b // a
if x >= c:
    print(c)
else:
    print(x)
