n=int(input())
a=[int(x) for x in input().split()]
arr=counter=0
for item in a:
    if abs(item+1)<=abs(item-1):
        arr+=abs(item+1)
        counter+=1
    else:
        arr+=abs(item-1)
if counter%2==1:
    if 0 in a:
        print(arr)
    else:
        print(arr+2)
else:
    print(arr)
        

