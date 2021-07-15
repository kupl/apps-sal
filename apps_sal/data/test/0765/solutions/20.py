t,s,q = input().split()
t=int(t)
s=int(s)
q=int(q)
r=s
m=1
while(r<t):
    r=r*q
    if(r<t):
        m+=1
print(m)

