n=int(input())
arr=[int(x) for x in input().split()]
arr=sorted(arr)
arr.reverse()
s=set()
sum=0
flag=0
for i in range(n):
    temp=arr[i]
    while temp in s:
        temp=temp-1
        if temp==0:
            flag=1
            break
    sum+=temp
    s.add(temp)
    if flag==1:
        break
print(sum)
