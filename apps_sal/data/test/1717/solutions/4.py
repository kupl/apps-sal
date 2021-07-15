import fractions
n = int(input())
ans = 2
for i in range(2, n+1):
    ans = ans * i // fractions.gcd(ans, i)
    
print(ans+1)
