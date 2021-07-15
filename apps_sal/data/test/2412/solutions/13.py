'''n=int(input())
s=input().rstrip()
p=input().rstrip().split(' ')
for i in range(0,n):
    o=int(input())
    u=input().rstrip().split(' ')'''

n=int(input())
for i in range(0,n):
    o=int(input())
    s=input().rstrip()
    x=list(s)
    if '8' not in x or len(x)<11:
        print("NO")
    else:
        f=x.index('8')
        g=x[f:len(x)]
        if len(g)>=11:
            print("YES")
        else:
            print("NO")

