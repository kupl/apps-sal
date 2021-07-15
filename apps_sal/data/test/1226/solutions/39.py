n,a,b=list(map(int,input().split()))
mod=10**9+7
sum=(pow(2,n,mod)-1)%mod
nume_a=1
deno_a=1
for i in range(n-a+1,n+1):
    nume_a=(nume_a*(i%mod))%mod
    deno_a=(deno_a*(i-(n-a+1)+1)%mod)%mod
ans_a=(nume_a*(pow(deno_a,mod-2,mod)))%mod
nume_b=1
deno_b=1
for i in range(n-b+1,n+1):
    nume_b=(nume_b*(i%mod))%mod
    deno_b=(deno_b*(i-(n-b+1)+1)%mod)%mod
ans_b=(nume_b*(pow(deno_b,mod-2,mod)))%mod
print(((sum-ans_a-ans_b)%mod))

