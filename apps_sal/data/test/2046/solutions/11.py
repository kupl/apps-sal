n=int(input())
s=set()
l=n
a=map(int,input().split())
for i in a:
    s.add(i)
    while l in s:
        print(l,end=' ')
        l-=1
    print()

