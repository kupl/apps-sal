input()
a=sum(list(map(int,input().split())))
b=-1
c=int(input())
for i in range(c):
    d,f=list(map(int,input().split()))
    if d<=a and a<=f:
        b=a
        break
    if a<=d:
        b=d
        break

print(b)

