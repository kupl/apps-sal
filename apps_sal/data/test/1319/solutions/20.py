readInts=lambda: list(map(int, input().split()))

n=int(input())
a=readInts()
p={}
for b in a:
    p[b]=p.get(b,0)+1

MOD=10**9+7
ret=1;cnt=1;
for x in list(p.items()):
    t=x[1]
    now=pow(x[0],(1+t)*t//2,MOD)
    ret*=pow(ret,t,MOD)
    ret%=MOD
    ret*=pow(now,cnt,MOD)
    ret%=MOD
    cnt=cnt*(t+1)
    cnt%=MOD-1
    
print(ret)



