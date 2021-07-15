p11 = input()
p12 = input()
p21 = input()
p22 = input()

s1 = (p11 + p12[1] + p12[0]).replace('X', '')
s2 = (p21 + p22[1] + p22[0]).replace('X', '')

if(s1 == 'ABC' or s1 == 'BCA' or s1 == 'CAB'):
    first = True
else:
    first = False
    
if(s2 == 'ABC' or s2 == 'BCA' or s2 == 'CAB'):
    second = True
else:
    second = False
    
    
if(first == second):
    print('YES')
else:
    print('NO')
