N=int(input())
li=[]
k=0
for i in range(N):
    a,b=list(map(int,input().split()))
    if a==b:
        k+=1
    else:
        k*=0
    if k==3:
        print("Yes")
        return
print("No")

