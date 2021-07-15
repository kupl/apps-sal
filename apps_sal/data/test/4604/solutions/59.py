n=int(input())
a=list(map(int,input().split()))
flag=0
A=a.sort()
num=[]

if n%2==0:
    for i in range(1,n,2):
        num.append(i)
        num.append(i)

if n%2==1:
    num=[0]
    for i in range(2,n,2):
        num.append(i)
        num.append(i)

if num==a:
    print(2**(n//2)%(10**9+7))

else:
    print("0")
