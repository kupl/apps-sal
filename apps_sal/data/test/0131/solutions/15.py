n=int(input())
l=list(map(int,input().strip().split()))
l1=list(map(int,input().strip().split()))
r=sum(l)
r1=sum(l1)
if (r1>r):
    print ("No")
else:
    print ("Yes")
