a = input()
b = input()


def remove_zeroes(s: str):
    i = 0
    for x in range(len(s) - 1):
        if s[x] == '0':
            i += 1
        else:
            break
    return s[i:]


a = remove_zeroes(a)
b = remove_zeroes(b)

if len(a) != len(b):
    if len(a) > len(b):
        print('>')
    else:
        print('<')
    return

cmp1 = a > b
cmp2 = a < b

if cmp1:
    print('>')
elif cmp2:
    print('<')
else:
    print('=')
