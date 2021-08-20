s = input().split()
x = int(s[0])
y = int(s[1])
if y < 1:
    print('No')
elif x == 0 and y > 1:
    print('No')
elif x != 0 and y <= 1:
    print('No')
elif y >= 1:
    if y - 1 > x:
        print('No')
    elif (x - y + 1) % 2 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
