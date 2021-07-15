a,b=map(int,input().split())
c=0
if (100*a)%8==0:
    w=(100*a)//8
else:
    w=((100*a)//8)+1
if (100*(a+1))%8==0:
    s=((100*(a+1))//8)-1
else:
    s=(100*(a+1))//8
for i in range(w,s+1):
    if i//10==b:
        print(i)
        c+=1
        break
    else:
        pass
if c==0:
    print(-1)
else:
    pass
