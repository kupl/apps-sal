t=int(input())
for i in ' '*t:
    n=int(input())
    if n%2==1:print('7'+'1'*((n-3)//2))
    else:print('1'*(n//2))
