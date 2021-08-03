a, b = list(map(str, input().split()))
c = int(a + b)
x = c**(1 / 2)
if x.is_integer():
    print('Yes')
else:
    print('No')
