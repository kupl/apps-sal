from collections import defaultdict
c = defaultdict(int)
m = defaultdict(list)
n = int(input())
for i in range(n):
    s,a = input().split()
    m[s].append(int(a))
    c[s]+=1
ali = c['10']
bob = c['01']
co = c['11']
no = c['00']

if(ali==0 or bob==0) and (co==0):
    print(0)
else:
    if(ali>bob):
        ali-=(ali-bob)
    else:
        bob-=(bob-ali)
    x = m['10']
    y = m['01']
    x.sort(reverse=True)
    y.sort(reverse=True)
    ans = sum(x[:ali])+sum(y[:ali])
    rem = x[ali:]+y[ali:]+m['00']
    tot = ali+bob
    if(co>0):
        ans+=sum(m['11'])
        tot+=co
        ali+=co
        bob+=co
    #print(ali,bob,tot)
    rem.sort(reverse=True)
    #print(rem)
    mn = min(ali,bob)
    re = max(2*mn-tot,0)
    #print(re)
    ans+=sum(rem[:re])
    print(ans)
    

