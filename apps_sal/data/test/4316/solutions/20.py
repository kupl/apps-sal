s = input()
a = 0
b = 0
c = 0
for i in range(1, 4):
    if ord(s[0]) == ord(s[i]):
        a = i
        b += 1
if b == 1:
    if a == 1:
        if ord(s[2]) == ord(s[3]):
            print('Yes')
        else:
            print('No')
    elif a == 2:
        if ord(s[1]) == ord(s[3]):
            print('Yes')
        else:
            print('No')
    elif a == 3:
        if ord(s[1]) == ord(s[2]):
            print('Yes')
        else:
            print('No')
else:
    print('No')
