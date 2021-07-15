n=int(input())
c=0
for i in range(2,int(n**0.5+1)):
    if n%i==0:
        c=1
        break
if c==0:print(1)
else:print((n-i)//2+1)
