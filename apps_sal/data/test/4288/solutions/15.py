a, b, c = list(map(int, input().split()))
if (a == b and b != c) or (a == c and a != b) or (b == c and a != b):
    print('Yes')
else:
    print('No')

