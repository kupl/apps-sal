n=int(input())
s=[]
a=[]
for i in range(n):
    s.append(input())
    p=0
    q=0
    for j in s[i]:
        if(j=='s'):
            p+=1
        elif(j=='h'):
            q+=1
    val=(q-p)/(q+p)
    a.append([val,i])
a.sort()
fin=''
for i in range(n):
    
    fin+=s[a[i][1]]
#print(fin)
p=0
q=0
ins=0
for i in fin:
    if(i=='s'):
        q+=1
    elif(i=='h'):
        p+=1
        ins+=q
print(ins)
    

