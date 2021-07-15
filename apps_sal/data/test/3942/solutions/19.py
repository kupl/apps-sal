s=input()
w=s.rindex("#")
q=0

for i in range(len(s)-1,w,-1) :
    if s[i]=="(" :
        q+=1
    else :
        q-=1
    if q>0 :
        print(-1)
        return
d=0
zz=[]
for i in range(w) :
    if s[i]=="(" :
        d+=1
    elif s[i]==")" :
        d-=1
    else :
        d-=1
        zz.append(1)
    if d<0 :
        print(-1)
        return
y=q+d
if y<=0 :
    print(-1)
else :
    zz.append(y)
    print("\n".join(map(str,zz)))
        
    

