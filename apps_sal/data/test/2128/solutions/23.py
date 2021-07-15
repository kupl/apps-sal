MOD =  998244353

def power(x,y):
    res=1
    while(y>0):
        if(y&1):
            res = x*res%MOD
        y = y >>1
        x = x*x%MOD
    return res



n = int(input())



prob = input().split()


p = power(100,n)
q = 1

for i in range(0,n-1):
    q = q*(int(prob[i]))%MOD
    p = (p + q*(power(100,n-i-1))%MOD)%MOD
q = q*(int(prob[n-1]))%MOD

print(p*(power(q,MOD-2))%MOD)
