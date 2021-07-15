a,s=input().split()
a=int(a)
s=int(s)
top1=a
top2=a
l1=[]
l2=[]
l3=[]
for i in range(0,100007):
    l1.append(0)
    l2.append(0)
for i in range(0,s):
    z,x=input().split()
    z=int(z)
    x=int(x)
    if l1[z]==0:
        top1-=1
        l1[z]=1
    if l2[x]==0:
        top2-=1
        l2[x]=1
    l3.append(top1*top2)
for i in l3:
    print(i,end=" ")
    

