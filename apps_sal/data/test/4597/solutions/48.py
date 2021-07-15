n = int(input())
mod = 1000000007
su = 1
for i in range(1,n+1):
    su = ((su%mod)*(i%mod))%mod
print(su%mod)
