(x, y) = input().split()
x = int(x)
y = int(y)
y -= 1
if y == 0 and x != 0:
    print('No')
elif y == -1:
    print('No')
else:
    x -= y
    if x % 2 == 0 and x >= 0:
        print('Yes')
    else:
        print('No')
