n,x=map(int,input().split())
markings=[0 for i in range(2**n-1)]
for i in range(1,2**n):
    #print(i,markings)
    if markings[i-1]==0 and (x^i)<(2**n) and i!=x:
        markings[(x^i)-1]=1 
if x<2**n:
    markings[x-1]=1
arr=[]
for i in range(2**n-1):
    if markings[i]==0:
        arr.append(i+1)
print(len(arr))
if len(arr)>0:
    print(arr[0],end=" ")
    for i in range(1,len(arr)):
        print(arr[i]^arr[i-1],end=" ")
    print("")
        

