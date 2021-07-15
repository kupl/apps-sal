str = input()

cnt = str.count('R')

if cnt == 3:
    print((3))
elif cnt == 2:
    if str[0] == str[2]:
        print((1))
    else:
        print((2))
elif cnt == 1:
    print((1))
else:
    print((0))

