n=int(input())
c=0
for i in range(2,n):
    if n//i==n/i:
        c=1
        print(str(i)+str(n//i))
        break
if c==0:
    print(str(1)+str(n))
    
    
        

