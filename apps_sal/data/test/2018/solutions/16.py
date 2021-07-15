from fractions import gcd

arr=[int(x) for x in input().split()]
t=gcd(arr[0],arr[1])
a=arr[0]//t
b=arr[1]//t
for i in range(arr[2]):
    nums=[int(x) for x in input().split()]
    w=nums[1]-1
    y=nums[3]-1
    if nums[0]==1:
        w=w//a
    else:
        w=w//b
    if nums[2]==1:
        y=y//a
    else:
        y=y//b
    if w==y:
        print("YES")
    else:
        print("NO")
