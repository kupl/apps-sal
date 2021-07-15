N=int(input())
A=list(map(int,input().split()))
a=[i for i in A if i%2==0]
b=len([i for i in a if i%3==0 or i%5==0])
if len(a)==b:
    print('APPROVED')
else:
    print('DENIED')
