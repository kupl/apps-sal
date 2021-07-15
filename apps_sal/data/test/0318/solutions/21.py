ip=str(input())
h=int(ip[0]+ip[1])
m=int(ip[3]+ip[4])
k=h*60+m
n=int(input())
k+=n
h1=(k//60)%24
m1=k%60
if h1<10:
    h1='0'+str(h1)
if m1<10:
    m1='0'+str(m1)
print(h1,end=':')
print(m1)

