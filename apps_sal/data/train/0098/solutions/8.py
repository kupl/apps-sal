n = int(input())
while n:
    a,b,c=map(int,input().split())
    if a<b:
        a,b=b,a
    print(min(b,(a+b+c)//3))
    n-=1
