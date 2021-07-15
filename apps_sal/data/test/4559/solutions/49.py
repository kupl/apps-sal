n=int(input())
a=list(map(int,input().split()))
s=1000000000000000000
k,c=1,0
for i in a:
    if k*i>s:
        c=1
        break
    k*=i
if 0 in a:
    print(0)
    
elif c==0:
    print(k)
else:
    print(-1)
