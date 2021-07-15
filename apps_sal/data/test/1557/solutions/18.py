h,a,c=list(map(int,input().split()))
h2,a2=list(map(int,input().split()))
count=1
S=[]
while(h2>a):
    count+=1
    if(h>a2):
        S.append('STRIKE')
        
        h2-=a
    else:
        S.append('HEAL')
        h+=c
    h-=a2
S.append('STRIKE')
print(count)
for i in S:
    print(i)

