n,a,b=map(int,input().split())


A=list(map(int,input().split()))

B=list(map(int,input().split()))

for i in range(n):
    if(i+1 in A):
        print(1,end=" ")
    else:
        print(2,end=" ")

