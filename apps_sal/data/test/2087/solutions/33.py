ans = 0
a,b,c=map(int,input().split())
def ss(n):
    return n*(n+1)//2
a = ss(a)
b = ss(b)
c = ss(c)
ans=a*b*c
print(ans%998244353)
