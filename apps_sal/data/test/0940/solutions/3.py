arr=[int(x) for x in input().split()]
arr.sort()
a=arr[0]
b=arr[1]
c=arr[2]
if(a+b>c):
    print(0)
else:
    print(c-a-b+1)
