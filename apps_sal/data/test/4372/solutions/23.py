import math
n=int(input())
arr=list(map(int,input().strip().split()))
x=max(arr)
a=[]
xx=x-arr[0]
for i in arr:
    ai=x-i
    a.append(ai)
    xx=math.gcd(xx,ai)
# print(a,xx)
print(sum(a)//xx,xx)
