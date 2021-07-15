n = int(input())
pf={}
for m in range(1,n+1):
    for i in range(2,int(m**0.5)+1):
        while m%i==0:
            pf[i]=pf.get(i,0)+1
            m//=i
    if m>1:
        pf[m]=pf.get(m,0)+1
ans = 0
for k , v in pf.items():
    if v >= 74:
        ans += 1
    if v >= 24:
        for s , t in pf.items():
            if s != k and t >= 2:
                ans += 1
    if v >= 14:
        for s , t in pf.items():
            if s != k and t >= 4:
                ans += 1
    if v >= 4:
        for s , t in pf.items():
            if s > k and t >= 4:
                for f , g in pf.items():
                    if f != s and f != k and g >= 2:
                        ans += 1
print(ans)
