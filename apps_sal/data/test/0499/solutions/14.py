import collections
import math

n = int(input())
s = input()
a, b, c = s.count('B'), s.count('G'), s.count('R')
if a * b * c != 0 or (a >= 2 and b >= 2) or (a >= 2 and c >= 2) or (c >= 2 and b >= 2):
    print('BGR')
elif a != 0 and b == 0 and c == 0:
    print('B')
elif a == 0 and b != 0 and c == 0:
    print('G')
elif a == 0 and b == 0 and c != 0:
    print('R')
elif a == 0:
    if b == c:
        print('B')
    elif b > c:
        print('BR')
    else:
        print('BG')
elif b == 0:
    if a == c:
        print('G')
    elif a > c:
        print('GR')
    else:
        print('BG')
elif c == 0:
    if b == a:
        print('R')
    elif b > a:
        print('BR')
    else:
        print('GR')
