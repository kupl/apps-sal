n=int(input(''))
m=list(input(''))


count=0
for i in range(n):
    if m[i]=='X': count+=1
if n/2==count:
    print('0')
    for i in range(n):
        print(m[i],end='')
if n/2>count:
    print(int(n/2-count))
    k=n/2-count
    for i in range(n):
        if m[i]=='x' and k>0:
            print('X',end='')
            k-=1;
        else: print(m[i],end='')
if n/2<count:
    print(int(count-n/2))
    k=count-n/2
    for i in range(n):
        if m[i]=='X' and k>0:
            print('x',end='')
            k-=1;
        else: print(m[i],end='')        
    





            
            
        
        
    


                


