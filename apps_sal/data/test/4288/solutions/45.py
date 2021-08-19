(a, b, c) = map(int, input().split())
if a == b and a == c:
    print('No')
elif a == b or a == c or b == c:
    print('Yes')
else:
    print('No')
