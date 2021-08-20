(a, b, c) = list(map(int, input().split()))
s = (a + b + c) / 2
if s == a or s == b or s == c:
    print('Yes')
else:
    print('No')
