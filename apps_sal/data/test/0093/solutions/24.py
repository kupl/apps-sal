a1 = input()
a2 = input()
b1 = input()
b2 = input()
bel = [a1,a2]
el = [b1,b2]
checker = False
for i in range(100):
    if not( a1 == b1 and a2 == b2):
        if 'X' in a1:
            if a1.find('X') == 0:
                a1 = a2[0]+a1[1]
                a2 = 'X'+a2[1]
            else:
                a1 = 'X'+a1[0]
                
            
          
        else:
            if a2.find('X') == 0:
                a2 = a2[1] + 'X'
            else:
                
                a2 = a2[0] + a1[1]
                a1 = a1[0] +'X'
                 
    else:
        
        
        checker = True
        break
if checker == True:
    print('YES')
else:
    print('NO')
