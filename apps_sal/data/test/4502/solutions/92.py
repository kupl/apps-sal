n=int(input())
a=list(map(int,input().split()))

if n%2==0:
    S=a[-1::-2]+a[::2]
    for x in S:
        print(x,end=' ')
else:
    S=a[-1::-2]+a[1::2]
    for x in S:
        print(x,end=' ')
print()

