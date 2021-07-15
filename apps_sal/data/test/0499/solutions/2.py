n = int(input())
s = input()
g = s.count('G')
b = s.count('B')
r = s.count('R')

if g != 0 and r != 0 and b != 0: print('BGR')
elif g==0 and r == 0: print('B')
elif g==0 and b == 0: print('R')
elif b==0 and r == 0: print('G')
elif g==0:
    
    if r >= 2: print('B',end = '')
    print('G',end = '')
    if b >= 2: print('R', end = '')
elif r==0:
    
    if g >= 2: print('B',end = '')
    if b >= 2: print('G', end = '')
    print('R',end = '')
elif b==0:
    print('B',end = '')
    if r >= 2: print('G',end = '')
    if g >= 2: print('R', end = '')
