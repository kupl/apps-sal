n=int(input())
a=input()
v=1
q=0
maxlen=0
for i in range(1,len(a)):
    if a[i]=='[':
        v+=1
    else:
        v-=1
    if(a[i-1]=='[' and a[i]==']'):
        q+=1
    maxlen=max(maxlen,v)
v=[[" "]*(q*3+n) for i in range(3+ (max(0,maxlen-1)*2))]
y=3+(max(0,maxlen-1)*2)
x=0
w=0
for i in range(n):
    if a[i]=='[':
        for j in range(w,y-w):
            if(j==w or j==y-1-w):
                v[j][x]='+'
                v[j][x+1]='-'
            else:
                v[j][x]='|'
        x+=1
        w+=1
    else:
        if(a[i-1]=='['):
            x+=3
        w-=1
        for j in range(w,y-w):
            if(j==w or j==y-1-w):
                v[j][x]='+'
                v[j][x-1]='-'
            else:
                v[j][x]='|'
        x+=1
for i in range(3+ (max(0,maxlen-1)*2)):
    for j in range(q*3+n):
        print(v[i][j],end="")
    print()    
