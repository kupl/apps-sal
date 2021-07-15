n,x=map(int,input().split())
s=0
l=1000
for i in range(n):
    m=int(input())
    s += m
    if m<l:
        l=m
x -= s
x //= l
print(n+x)
