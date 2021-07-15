a = int(input())
b = list(map(int,input().split()))
c = b[0]%998244353
d = b[0]%998244353
for i in range(1,a):
    c = (2*c + d + b[i])%998244353
    d = (2*d + b[i])%998244353
print(c)
