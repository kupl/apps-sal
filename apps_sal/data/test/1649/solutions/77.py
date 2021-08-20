(a, b, c, d) = map(int, input().split())
if a == b + c + d:
    print('Yes')
elif b == a + c + d:
    print('Yes')
elif c == a + b + d:
    print('Yes')
elif d == a + b + c:
    print('Yes')
elif a + b == c + d:
    print('Yes')
elif a + c == b + d:
    print('Yes')
elif a + d == b + c:
    print('Yes')
elif b + c == c + d:
    print('Yes')
elif b + d == a + d:
    print('Yes')
else:
    print('No')
