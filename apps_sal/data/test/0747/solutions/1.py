n,x=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    t,h,m=list(map(int,input().split()))
    if t:
        a.append((h,m))
    else:
        b.append((h,m))
counter1=0;
now=True
a1=a[:]
b1=b[:]
x2=x
while 1:
    if now:
        if(len(a)==0):
            break;
        
        i=0
        maxx=0
        mi=0
        for kor in a:
            if kor[0]<=x and maxx<kor[1]:
                maxx=kor[1]
                mi=i
            i+=1
        if maxx==0:
            break
        x+=maxx
        a.pop(mi)
        counter1+=1
        now=False
    else:
        if(len(b)==0):
            break;
        i=0
        maxx=0
        mi=0
        for kor in b:
            if kor[0]<=x and maxx<kor[1]:
                maxx=kor[1]
                mi=i
            i+=1
        if(maxx==0):
            break;
        x+=maxx
        b.pop(mi)
        counter1+=1
        now=True
    
counter2=0;
now=False
while 1:
    if now:
        if(len(a1)==0):
            break;
        i=0
        maxx=0
        mi=0
        for kor in a1:
            if kor[0]<=x2 and maxx<kor[1]:
                maxx=kor[1]
                mi=i
            i+=1
        if maxx==0:
            break
        x2+=maxx
        a1.pop(mi)
        counter2+=1
        now=False
    else:
        if(len(b1)==0):
            break;
        i=0
        maxx=0
        mi=0
        for kor in b1:
            if kor[0]<=x2 and maxx<kor[1]:
                maxx=kor[1]
                mi=i
            i+=1
        if(maxx==0):
            break;
        x2+=maxx
        b1.pop(mi)
        counter2+=1
        now=True
print(counter1 if counter1>counter2 else counter2) 















        

