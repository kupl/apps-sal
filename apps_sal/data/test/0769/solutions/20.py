a,b,c=map(int,input().split())
s=set()
a*=10
i=1
while True:
    if c==(a//b):
        print(i)
        return
    a=(a-(a//b)*b)*10
    i+=1
    if i>150000:
        print(-1)
        return
