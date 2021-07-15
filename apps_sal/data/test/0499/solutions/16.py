n = int(input())
s = input()
b = 0
g = 0
r = 0
for i in range(n):
    if s[i] == 'B':
        b += 1
    elif s[i] == 'G':
        g += 1
    else:
        r += 1
if b == 0:
    if g == 0:
        print('R')
    elif r == 0:
        print('G')
    elif g == 1:
        if r == 1:
            print('B')
        else:
            print('BG')
    elif r == 1:
        print('BR')
    else:
        print('BGR')
elif g == 0:
    if b == 0:
        print('R')
    elif r == 0:
        print('B')
    elif b == 1:
        if r == 1:
            print('G')
        else:
            print('BG')
    elif r == 1:
        print('GR')
    else:
        print('BGR')
elif r == 0:
    if b == 0:
        print('G')
    elif g == 0:
        print('B')
    elif b == 1:
        if g == 1:
            print('R')
        else:
            print('BR')
    elif g == 1:
        print('GR')
    else:
        print('BGR')
else:
    print('BGR')
