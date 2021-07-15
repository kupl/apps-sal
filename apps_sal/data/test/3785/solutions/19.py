n,m,k=list(map(int,input().split()))
M=[input() for i in range(n)]
T=[[] for i in range(n)]
p=0
for i in range(n) :
    for j in range(m) :
        if M[i][j]=='#' :
            T[i].append(M[i][j])
        else :
            T[i].append('X')
for i in range(n) :
    p=p+M[i].count('#')
for i in range(n) :
    for j in range(m) :
        if M[i][j]=='.' :
            a=i
            b=j
            break
t=(n*m)-p-k
l=[[a,b]]
T[a][b]='.'
t=t-1
while t>0  :
    r=l[0]
    
    del(l[0])
    i=r[0]
    j=r[1]
  
    if i+1!=n  :
        if M[i+1][j]=='.' and T[i+1][j]!='.'  :
            l.append([i+1,j])
            T[i+1][j]='.'
            t=t-1
    if t<=0 :
        break
    if i-1!=-1  :
        if M[i-1][j]=='.' and T[i-1][j]!='.'  :
            l.append([i-1,j])
            T[i-1][j]='.'
            t=t-1
    if t<=0 :
        break
    if j+1!=m  :
        if M[i][j+1]=='.' and  T[i][j+1]!='.'  :
            l.append([i,j+1])
            T[i][j+1]='.'
            t=t-1
    if t<=0 :
        break
    if j-1!=-1  :
        if M[i][j-1]=='.' and  T[i][j-1]!='.' :
            l.append([i,j-1])
            T[i][j-1]='.'
            t=t-1
            
for i in range(n) :
    S=''
    for j in range(m) :
        S=S+T[i][j]
    print(S)

