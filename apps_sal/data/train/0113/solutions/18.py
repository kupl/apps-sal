n=int(input())
for i in range(n):
    a,b=[int(x) for x in input().split(' ')]
    c=abs(a-b)
    d=0
    d+=int(c/5)
    c=c%5
    d+=int(c/2)
    c=c%2
    d+=c
    print(d)

