l1=list(str(input()))
l2=list(str(input()))
n=len(l1)
count=0
for i in range(n-1):
    if l1[i]=='0' and l1[i+1]=='0':
        if l2[i]=='0':
            l1[i],l1[i+1],l2[i]='X','X','X'
            count+=1
        elif l2[i+1]=='0':
            l1[i],l1[i+1],l2[i+1]='X','X','X'
            count+=1
    if l2[i]=='0' and l2[i+1]=='0':
        if l1[i]=='0':
            l2[i],l2[i+1],l1[i]='X','X','X'
            count+=1
        elif l1[i+1]=='0':
            l2[i],l2[i+1],l1[i+1]='X','X','X'
            count+=1
print(count)
