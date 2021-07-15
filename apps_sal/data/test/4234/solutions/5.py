n=int(input())
s=input()
l1=[]
for c in s:
    if len(l1)==0:
        l1.append(c)
    else :
        if len(l1)%2==1:
            if l1[-1]==c:
                continue
            else :
                l1.append(c)
        else :
            l1.append(c)
            
if len(l1)%2==0:
    print(n-len(l1))
    print(''.join(l1))
else :
    print(n-len(l1)+1)
    print(''.join(str(l1[i]) for i in range(0,len(l1)-1)))
