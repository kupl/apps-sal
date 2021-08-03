v = 'aeiou'

a = input()
b = input()

ans = True
if (len(a) == len(b)):

    for i in range(len(a)):
        x = a[i]
        y = b[i]

        q = x in v
        w = y in v

        if (q ^ w):
            ans = False

    if ans:
        print('Yes')
    else:
        print('No')
else:
    print('No')
