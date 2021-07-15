v=list((input().split()))
n=int(v[0])
m=int(v[1])
v=list()
for i in range(n):
    v.append(input())
if n==1:
    print(0)
    return
kll=0
j=0
brk=0
while j<m:
    for i in range (1,n):
        if v[i][:j+1]<v[i-1][:j+1]:
            brk=1
            break
    if brk:
        for i in range(n):
            tmp=list(v[i])
            tmp.pop(j)
            v[i]="".join(tmp)
        kll+=1
        m-=1
    else:
        j+=1
    brk=0
print(kll)
