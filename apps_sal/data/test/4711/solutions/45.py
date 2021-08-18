
a, b, c = map(int, input().split())

if a >= b and a >= c:
    print(b + c)
elif b >= a and b >= c:
    print(a + c)
elif c >= a and c >= b:
    print(a + b)
