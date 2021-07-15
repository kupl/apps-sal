n=input().split()
m=int(n[1])
n=int(n[0])
if m<n:
    c=m
    m=n
    n=c
c=''
a=bin(m)[2:]
b=bin(n)[2:]
b='0'*(len(a)-len(b))+b
while a[0]==b[0] and len(a)!= 0:
    c1 = str(int(a[0])^int(b[0]))
    c+=c1
    a=a[1:]
    b=b[1:]
    if len(a)==0 or len(b)==0:
        break
    #if len(a)!=0:
     #   a=str(int(a))
    #if len(b)!=0:
     #7   b=str(int(b))
aa=max(len(b),len(a))
c=c+aa*'1'
c=int(c)
d=1
p=0
while c!=0:
    s=c%10
    p+=d*s
    d=d*2
    c=c//10
print(p)

 

