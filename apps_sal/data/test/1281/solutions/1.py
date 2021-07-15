from math import *
#n,k=map(int,input().split())
#A = list(map(int,input().split()))
n,k = map(int,input().split())
ans = [0] * n
#^xor
lul = 2**k - 1
A = list(map(int,input().split()))
ans[0]  = A[0]
for j in range(1, n):
    ans[j] = ans[j-1]^A[j]
#print(ans)
d = dict()
for j in range(n):
    if ans[j] in d:
        d[ans[j]]+=1;
    else:
        d[ans[j]] = 1
#print(d)
ans =0
def huy(n):
    return n*(n-1)//2
for j in d:
    now = d[j]
    #print(d[j],j)
    xor = lul^j
    cur = now

    if xor in d :

        now2 = d[xor]
        #print(now,xor)
        cur += now2



        ans += huy(cur//2+cur%2)
        ans+=huy(cur//2)
        if j ==0:
            ans+=2*(cur//2)
    else:
        if(j==0 or xor ==0):
            ans+= 2*(cur//2)
        ans += 2*huy(cur // 2 + cur % 2)
        ans += 2*huy(cur // 2)
print(huy(n+1) - ans//2)
