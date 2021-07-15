S=list(input())
c=0;m=''
for i in S:
    if i!=m:
        m=i
        c+=1
print(c-1)
