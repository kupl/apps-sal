a, b, c = list(map(int, input().split()))

if a == b and a != c:
    print('Yes')
elif b == c and b != a:
    print('Yes')
elif c == a and c != b:
    print('Yes')
else:
    print('No')

