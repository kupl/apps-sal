n = int(input())
if n%2==1:
    print("-1")
else:
    for i in range(1,n,2):
        print(i+1,i,sep=" ",end=" ")

