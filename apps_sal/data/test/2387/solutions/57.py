n=int(input())
s1=0
s2=0
s3=list()
s4=list()
s5=list()
for i in range(n):
    a=str(input())
    b=str()
    while a!=b:
        b=a
        a=a.replace(r'()','')
    if len(a)==0:
        continue
    if a[0]=="(" and a[-1]=="(":
        s1+=len(a)
    elif a[0]==")" and a[-1]==")":
        s2+=len(a)
    else:
        x=len(a.replace("(",""))
        y=len(a)-x
        if x<y:
            s3.append([x,y])
        elif x==y:
            s4.append(x)
        else:
            s5.append([x,y])
            
s3.sort(key=lambda x:x[0])
s5.sort(key=lambda x:x[1])

flag=0
limit=s1

if len(s3)!=0:
    for i in range(len(s3)):
        if limit>=s3[i][0]:
            limit=limit-s3[i][0]+s3[i][1]
        else:
            flag=1
            print("No")
            break

x=limit

if len(s4)!=0:
    if limit<max(s4):
        print("No")
        flag=1

limit=s2
if len(s5)!=0:    
    if flag==0:
        for i in range(len(s5)):
            if limit>=s5[i][1]:
                limit=limit-s5[i][1]+s5[i][0]
            else:
                flag=1
                print("No")
                break

if flag==0 and len(s4)!=0:
    if limit<max(s4):
        print("No")
        flag=1

if flag==0 and x==limit:
    print("Yes")
elif flag==0:
    print("No")
        
        
       

