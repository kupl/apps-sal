a=int(input())

b=list(map(int,input().split()))

if sum(b)%a!=0:
    print(a-1)
else:
    print(a)

