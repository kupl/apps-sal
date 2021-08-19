(a, b, c) = map(int, input().split())
if a >= b and a >= c:
    print(a * 10 + b + c)
elif b >= a and b >= c:
    print(b * 10 + a + c)
else:
    print(c * 10 + a + b)
