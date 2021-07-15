a,b = map(int, input().split())
n = int((1+(1+8*(a+b))**0.5)/2-1)
con = [x for x in range(1, n+1)]
con=con[::-1]
con1=[]
con2=[]
a1=a
b1=b
a=max(a,b)
b=min(a1,b1)



for i in range(0,len(con)):
    if a-con[i]>0:
        con1.append(con[i])
        a-=con[i]
        con[i]=0
    elif a-con[i]==0:
        con1.append(con[i])
        con[i]=0
        break
        
con2=[]        
     
for i in con:
    if i!=0:
        con2.append(i)

a2=len(con1) 
b2=len(con2)    
huy=con1[::-1]
huy1=con2[::-1]    
if a1<=b1:
    print(b2)
    print(*huy1)

    print(a2)
    print(*huy)
else:
    print(a2)
    print(*huy)    
    print(b2)
    print(*huy1)    
