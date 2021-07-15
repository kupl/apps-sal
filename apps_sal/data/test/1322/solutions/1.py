import cmath
n = int(input())
q=1
p=1
def inv(a,b):
    if(a>1):
        return b-inv(b%a,a)*b//a
    else:
        return 1
for j in range(1,n+2):
    p=p*(n+1+j)% 1000000007
    q=(q*j)% 1000000007

print(p*inv(q,1000000007) % 1000000007 -1)
