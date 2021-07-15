def Ten_to_n(X, n):
    if (int(X/n)):
        return Ten_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

n=int(input())
wit=[1]
res=n
for i in range(n+1):
    cnt=0
    j=n-i
    si=Ten_to_n(i,6)
    for i in si:
        cnt+=int(i)
    ni=Ten_to_n(j,9)
    for i in ni:
        cnt+=int(i)
    res=min(res,cnt)
print(res)
