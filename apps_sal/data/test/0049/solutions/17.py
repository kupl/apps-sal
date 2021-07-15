k=int(input())
a=[]
for i in range(0,12):
    s=9*pow(10,i)*(i+1)
    if k<=s:
        break
    else:
        k-=s
pos=i+1
num=(pow(10,pos-1)+(k//pos)-1)
if k%pos==0:
    print(str(num)[-1])
else:
    print(str(num+(0 if pos==1 else 1))[(k%pos)-1])
 

