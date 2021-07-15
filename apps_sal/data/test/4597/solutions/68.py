#ABC055B
n = int(input())
ans = 1
MOD = 10**9+7
for i in range(2,n+1):
    ans*=i
    ans = ans%MOD
print(ans)    
