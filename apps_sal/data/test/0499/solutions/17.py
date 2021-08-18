
n = int(input())
s = input()

b, g, r = 0, 0, 0
for i in range(0, len(s)):
    if s[i] == 'B':
        b += 1
    elif s[i] == 'G':
        g += 1
    elif s[i] == 'R':
        r += 1
    else:
        assert False

if b != 0 and g == 0 and r == 0 or \
        b == 0 and g == 1 and r == 1:
    print('B')
elif b == 0 and g != 0 and r == 0 or \
        b == 1 and g == 0 and r == 1:
    print('G')
elif b == 0 and g == 0 and r != 0 or \
        b == 1 and g == 1 and r == 0:
    print('R')
elif b > 1 and g == 1 and r == 0 or\
        b > 1 and g == 0 and r == 1:
    print('GR')
elif b == 0 and g > 1 and r == 1 or\
        b == 1 and g > 1 and r == 0:
    print('BR')
elif b == 0 and g == 1 and r > 1 or\
        b == 1 and g == 0 and r > 1:
    print('BG')
else:
    print('BGR')
