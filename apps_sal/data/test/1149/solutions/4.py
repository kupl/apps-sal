n=int(input())
p=list(int(x) for x in input().split())[1:]
q=list(int(x) for x in input().split())[1:]
k=0
#print (p,q)
for i in range(1,n+1):
    if (i in p) or (i in q):
        k+=1
if k==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

