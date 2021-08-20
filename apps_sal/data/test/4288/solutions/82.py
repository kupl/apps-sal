(a, b, c) = map(int, input().split())
if a == b and b == c or (not a == b and (not b == c) and (not a == c)):
    print('No')
else:
    print('Yes')
