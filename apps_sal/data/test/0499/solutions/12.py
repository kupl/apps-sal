a = int(input())
per = input()
r = 0
g=0
b=0
for i in per:
    if i == 'R':
        r+=1
    if i == 'G':
        g+=1
    if i == 'B':
        b+=1

if r !=0 and b!=0 and g !=0:
    print('BGR')
elif r == 0 and b ==0:
    print('G')
elif r == 0 and g == 0:
    print('B')
elif g == 0 and b == 0:
    print('R')
elif r == 0:
    if g > 1:
        print('B', end='')    
    
    if b > 1:
        
        print('G', end ='')
    print('R', end = '')
    
elif g == 0:
    if r > 1:
        print('B',end ='')   
    print('G', end='')
    if b > 1:
        print('R', end ='')    
    
    
    
    
elif b == 0:
    print('B', end = '')
    if r > 1:
        print('G', end ='')    
    if g > 1:
        print('R', end='')    
    
    
    
    
