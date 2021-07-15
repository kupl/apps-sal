def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if(n%2):
        return func(n//2)*2+(n//2)+1
    else:
        return func(n//2)*2+(n//2)
n=int(input())
a=[1,2,1,4,1,2,1,8,1,2,1,4,1,2,1]

print(func(n-1))

