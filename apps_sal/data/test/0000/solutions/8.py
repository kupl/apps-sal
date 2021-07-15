s=input()
pos1=-1
pos2=-1
pos3=-1
pos4=-1
for i in range(0,len(s)):
    if(s[i]=='['):
        pos1=i
        break
for i in range(len(s)-1,pos1,-1):
    if(s[i]==']'):
        pos2=i
        break
for i in range(pos1,pos2+1):
    if(s[i]==':'):
        pos3=i
        break
for i in range(pos2,pos3,-1):
    if(s[i]==':'):
        pos4=i
        break
    
if(pos1==-1 or pos2==-1 or pos3==-1 or pos4==-1 or len(s)<4):
    print('-1')
else:
    c=0
    for j in range(pos3,pos4):
        if(s[j]=='|'):
            c=c+1
    print(c+4)

