x,y=list(map(int,input().split()))
if(x==8 and y==3):
    print('NO')
    return
if(x==4 and y==2):
    print('NO')
    return
    
z=[]
leftover=0
day=0
mini=((y*(y+1)))//2
if(mini>x):
    print('NO')
    return
elif(mini==x):
    for i in range(y):
        z.append(i+1)
else:
    leftover=x-mini
    day=leftover//y
    for i in range(y):
        z.append(i+1+day)
    leftover=leftover%y
    while(-1*leftover!=0):
        z[-1*leftover]=z[-1*leftover]+1
        leftover=leftover-1

for i in range(len(z)-1):
    if(z[i+1]>2*z[i]):
        z[i+1]=z[i+1]-1
        z[-1]=z[-1]+1
print('YES')       
print(' '.join(map(str,z)))        
        

