x=int(input())
y=[int(p) for p in input().split()]


x=a=y.count(5)
b=y.count(0)
while((x*5)%9!=0):
        x-=1
if(y.count(0)==0):
        print(-1)

elif(a!=0 and x!=0):
        print('5'*x+'0'*b)
elif(x==0):
        print(0)

