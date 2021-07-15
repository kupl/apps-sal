n = int(input())
MOD = 10**9+7

p = 1
for i in range(1, n+1):
    p *= i
    p %= MOD
    
print(p)
