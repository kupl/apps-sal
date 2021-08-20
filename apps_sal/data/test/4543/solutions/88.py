(a, b) = map(str, input().split())
c = int(a + b)
d = int(c ** 0.5)
if d ** 2 == c:
    print('Yes')
else:
    print('No')
