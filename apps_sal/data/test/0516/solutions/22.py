a,b=map(int,input().split())
s=str(input())
t=str(input())
m=0
ind=0
for i in range(b-a+1):
    a1=list(t[i:i+a])
    a2=list(s)
    #print(a1,a2)
    c=0
    for j in range(a):
        #print(i,j)
        if a1[j]==a2[j]:
            c+=1
    #print(c)
    if c>m:
        m=c
        ind=i
l1=list(t[ind:ind+a])
a3=list(s)
print(a-m)
for i in range(a):
    if a2[i]!=l1[i]:
        print(1+i,end=' ')
            
