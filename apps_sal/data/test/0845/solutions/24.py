def newR(str, charx):
    indx = str.index(charx)
    return str[indx - 1]


def newL(str, charx):
    indx = str.index(charx)
    return str[indx + 1]


one = 'qwertyuiop'
two = 'asdfghjkl;'
three = 'zxcvbnm,./'
a = input()
if a == 'R':
    finalstr = ''
    string = input()
    for i in string:
        if i in one:
            finalstr += newR(one, i)
        elif i in two:
            finalstr += newR(two, i)
        else:
            finalstr += newR(three, i)
    print(finalstr)
if a == 'L':
    finalstr = ''
    string = input()
    for i in string:
        if i in one:
            finalstr += newL(one, i)
        elif i in two:
            finalstr += newL(two, i)
        else:
            finalstr += newL(three, i)
    print(finalstr)
