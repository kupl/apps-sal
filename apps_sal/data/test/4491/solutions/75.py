n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
max=0
for i in range(n):
    tmp=sum(a[:i+1])
    tmp+=sum(b[i:])
    if max<tmp:
        max=tmp
print(max)
