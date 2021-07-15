import sys

s = input()
a = 0
b = 0
c = 0
state = 'a'
for i in s:
    if state == 'a':
        if i == 'a':
            a += 1
        elif i == 'b':
            b += 1
            state = 'b'
        elif i == 'c':
            state = 'c'
            c += 1
        else:
            print("NO")
            return
    elif state == 'b':
        if i == 'a':
            print("NO")
            return
        elif i == 'b':
            b += 1
        elif i == 'c':
            state = 'c'
            c += 1
        else:
            print("NO")
            return
    elif state == 'c':
        if i == 'a':
            print("NO")
            return
        elif i == 'b':
            print("NO")
            return
        elif i == 'c':
            state = 'c'
            c += 1
        else:
            print("NO")
            return
if a == 0 or b == 0 or (c != a and c != b):
    print("NO")
else:
    print("YES")

