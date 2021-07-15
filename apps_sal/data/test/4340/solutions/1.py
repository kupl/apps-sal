n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if(l[i]%2==0):
        print(l[i]-1,end=" ")
    else:
        print(l[i],end=" ")

