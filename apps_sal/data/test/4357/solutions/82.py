(a, b, c) = map(int, input().split())
if a <= b and b <= c:
    print(int(str(c) + str(b)) + a)
elif c <= b and b <= a:
    print(int(str(a) + str(b)) + c)
elif a <= c and c <= b:
    print(int(str(b) + str(c)) + a)
elif b <= c and c <= a:
    print(int(str(a) + str(c)) + b)
elif b <= a and a <= c:
    print(int(str(c) + str(a)) + b)
else:
    print(int(str(b) + str(a)) + c)
