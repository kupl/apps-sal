(a, b) = input().split()
c = input()
a = int(a)
b = int(b)
d = 0
if c[a] == '-':
    for i in range(a + b + 1):
        if c[i] == '-':
            d = d + 1
    if d == 1:
        print('Yes')
    else:
        print('No')
else:
    print('No')
