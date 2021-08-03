a = int(input())
b = str(a)
c = list(map(int, b))
d = sum(c)
if d % 9 == 0:
    print('Yes')
else:
    print('No')
