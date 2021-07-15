H,N= list(map(int,input().split())) 
A= list(map(int,input().split())) 

life=H
for i in range(N):
    life-=A[i]
    
if life<=0:
    print('Yes')
else:
    print('No')
