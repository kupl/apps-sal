(a, b, c) = list(map(int, input().split()))
if a + b == c:
    print('Yes')
elif a + c == b:
    print('Yes')
elif c + b == a:
    print('Yes')
else:
    print('No')
