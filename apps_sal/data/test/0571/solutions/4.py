import sys


def check(s):
    status = 0
    for char in s[:-1]:
        if char == '(':
            status += 1
        else:
            status -= 1
        if status <= 0:
            return ':('
    return s


n = int(input())
s = input()
if n % 2 != 0:
    print(':(')
else:
    leftcount = 0
    rightcount = 0
    for char in s:
        if char == '(':
            leftcount += 1
        if char == ')':
            rightcount += 1
    needed = n // 2
    if max(leftcount, rightcount) > needed:
        print(':(')
    else:
        leftneeded = (n // 2) - leftcount
        leftadded = 0
        newchars = []
        for char in s:
            if char == '?':
                if leftadded < leftneeded:
                    newchars.append('(')
                    leftadded += 1
                else:
                    newchars.append(')')
            else:
                newchars.append(char)
        print(check(''.join(newchars)))
