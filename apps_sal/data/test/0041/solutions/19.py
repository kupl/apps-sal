n=int(input())
a=list(input().split())
b=[i for i in range(n) if a[i]=="0"]
c=""
j=0
for i in range(n):
    if b[0]>=i:
        t=b[0]-i
        c+="{} ".format(t)
    elif j!=len(b)-1:
        t=min(abs(i-b[j]),abs(i-b[j+1]))
        if t==0:
            j+=1
        c+="{} ".format(t)
    else:
        c+="{} ".format(i-b[j])
print(c)
    

