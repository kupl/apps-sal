a, b, c = map(int, input().split())

if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
    print('Yes')
else:
    print('No')
